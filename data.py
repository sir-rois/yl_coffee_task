import sqlite3


class Data:
    def __init__(self):
        self.connection = sqlite3.connect('data/coffee.sqlite')
        self.cursor = self.connection.cursor()
        data = self.cursor.execute('SELECT * FROM coffee').fetchall()

        self.data = {}
        for e in data:
            self.data[e[0]] = list(e[1:])

    def __del__(self):
        self.connection.close()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(([k] + v for k, v in self.data.items()))

    def __getitem__(self, k):
        return [k] + self.data[k]

    def create(self, data):
        self.cursor.execute(
            """
            INSERT INTO coffee (sort_name, roast_degree, ground_or_whole, taste_description, price, package_volume)
            VALUES
                (?,?,?,?,?,?)
            """,
            data,
        )
        res = self.cursor.execute('SELECT last_insert_rowid()').fetchone()
        self.data[res[0]] = data
        self.connection.commit()

    def update(self, id, data):
        self.cursor.execute(
            """
            UPDATE coffee SET sort_name=?, roast_degree=?, ground_or_whole=?, taste_description=?, price=?, package_volume=?
            WHERE id = ?
            """,
            data + [id],
        )
        self.data[int(id)] = data
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute(
            """
            DELETE FROM coffee
            WHERE id = ?
            """,
            [id],
        )
        del self.data[int(id)]
        self.connection.commit()
