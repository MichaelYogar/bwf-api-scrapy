# Define your item pipelines here
import os
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta



# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class BwfCrawlerPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user=os.environ.get('DB_USER'),
            passwd=os.environ.get('DB_PASS'),
            database=os.environ.get('DB_NAME')
        )

        self.cursor = self.conn.cursor()

    def create_table(self):
        TABLES = {}

        TABLES["MEN'S DOUBLES"] = (
            "CREATE TABLE `MEN'S DOUBLES` ("
            "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            "  `points` varchar(100) NOT NULL,"
            "  `player_rank` varchar(100) NOT NULL,"
            "  `country` varchar(100) NOT NULL,"
            "  `win_loss` varchar(100) NOT NULL,"
            "  `parsed_url` varchar(100) NOT NULL,"
            "  `rank_change` varchar(100) NOT NULL,"
            "  `category` varchar(100) NOT NULL,"
            "  `player_name` varchar(100) NOT NULL,"
            "  `prize` varchar(100) NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")

        TABLES["WOMEN'S DOUBLES"] = (
            "CREATE TABLE `WOMEN'S DOUBLES` ("
            "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            "  `points` varchar(100) NOT NULL,"
            "  `player_rank` varchar(100) NOT NULL,"
            "  `country` varchar(100) NOT NULL,"
            "  `win_loss` varchar(100) NOT NULL,"
            "  `parsed_url` varchar(100) NOT NULL,"
            "  `rank_change` varchar(100) NOT NULL,"
            "  `category` varchar(100) NOT NULL,"
            "  `player_name` varchar(100) NOT NULL,"
            "  `prize` varchar(100) NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")

        TABLES["WOMEN'S SINGLES"] = (
            "CREATE TABLE `WOMEN'S SINGLES` ("
            "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            "  `points` varchar(100) NOT NULL,"
            "  `player_rank` varchar(100) NOT NULL,"
            "  `country` varchar(100) NOT NULL,"
            "  `win_loss` varchar(100) NOT NULL,"
            "  `parsed_url` varchar(100) NOT NULL,"
            "  `rank_change` varchar(100) NOT NULL,"
            "  `category` varchar(100) NOT NULL,"
            "  `player_name` varchar(100) NOT NULL,"
            "  `prize` varchar(100) NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")

        TABLES["MEN'S SINGLES"] = (
            "CREATE TABLE `MEN'S SINGLES` ("
            "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            "  `points` varchar(100) NOT NULL,"
            "  `player_rank` varchar(100) NOT NULL,"
            "  `country` varchar(100) NOT NULL,"
            "  `win_loss` varchar(100) NOT NULL,"
            "  `parsed_url` varchar(100) NOT NULL,"
            "  `rank_change` varchar(100) NOT NULL,"
            "  `category` varchar(100) NOT NULL,"
            "  `player_name` varchar(100) NOT NULL,"
            "  `prize` varchar(100) NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")

        TABLES["MIXED DOUBLES"] = (
            "CREATE TABLE `MIXED DOUBLES` ("
            "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            "  `points` varchar(100) NOT NULL,"
            "  `player_rank` varchar(100) NOT NULL,"
            "  `country` varchar(100) NOT NULL,"
            "  `win_loss` varchar(100) NOT NULL,"
            "  `parsed_url` varchar(100) NOT NULL,"
            "  `rank_change` varchar(100) NOT NULL,"
            "  `category` varchar(100) NOT NULL,"
            "  `player_name` varchar(100) NOT NULL,"
            "  `prize` varchar(100) NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("table already exists")
                else:
                    print(err.msg)
            else:
                print("OK")

    def store_db(self, item):
        category = item['category']
        
        add_api = (f"INSERT INTO `{category}` "
                "(player_rank, country, player_name, prize, win_loss, parsed_url, points, rank_change, category) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        player_data = (item['rank'], item['country'], item['player'], item['prize'], item['win_loss'],item['parsed_url'], item['points'], item['rank_change'], item['category'])
        self.cursor.execute(add_api, player_data)
        self.conn.commit()


    def process_item(self, item, spider):
        self.store_db(item)
        return item
