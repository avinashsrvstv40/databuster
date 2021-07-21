import xml.etree.ElementTree as ET


def get_attr_number(node):
    cnt_attrib = 0
    for child in node.iter():
        print(child)
        if child.attrib:
            cnt_attrib += len(child.attrib)
    return cnt_attrib

if __name__ == '__main__':

    data='''<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
    <entry>
        <author gender='male'>Harsh</author>
        <question type='hard'>XML 1</question>
        <description type='text'>This is related to XML parsing</description>
    </entry>
    </feed>
    '''

    myroot = ET.fromstring(data)
    print("The number of attributes in XML is:",get_attr_number(myroot))