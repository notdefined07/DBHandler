import sqlite3

conn = sqlite3.connect("calci9.db")
c = conn.cursor()

def table_creator():
    c.execute("CREATE TABLE IF NOT EXISTS calci_db5(OPERATOR_EXPRESSION TEXT,DATE_TIME TEXT)");
table_creator()
def data_entry(msg):
    c.execute(msg)
    conn.commit()
    #conn.close()


def data_show_db5():
    c.execute("select * from calci_db5")
    global a
    a=(len(c.fetchall()))

    return c.fetchall()

#if __name__ == "__main__":
    #data_entry("INSERT INTO calci_db4(OPERATOR_EXPRESSION,DATE_TIME) VALUES('5*a,operant should be integar', '2019-01-17 11:49:54')")
    #print(data_show("select * from calci_db5"))



def data_compare():
    c.execute("select * from calci_db5")
    global b
    b=(len(c.fetchall()))
    if b>a:
        print("data saved sucessfully")
    else:
        print("data not saved suceessfully")


