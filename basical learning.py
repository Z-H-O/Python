import xlsxwriter
data=[['Name', 'Web', 'Content'],['Alice', 'https://example.com/alice', 'This is Alice\'s content.'],['Bob', 'https://example.com/bob', 'This is Bob\'s content.']]
xlsx = xlsxwriter.Workbook('python.xlsx')
sheet = xlsx .add_worksheet('Sheet1')
sheet.write_row('A1', data[0])
xlsx.close()