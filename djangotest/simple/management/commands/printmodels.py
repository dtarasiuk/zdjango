from django.core.management.base import NoArgsCommand
from django.db import connection

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        result = ''
        connection_cursor = connection.cursor()
        for table in connection.introspection.get_table_list(connection_cursor):
            result += "class %s(models.Model)" % self.get_model_name(table)
            connection_cursor.execute("SELECT count(*) from %s" % table)
            count = connection_cursor.fetchall()
            result += "Objects: %s\n" % count[0]
        print result
        
    def get_model_name(self, table):
        return table.title().replace('_','').replace(' ','').replace('-','')
