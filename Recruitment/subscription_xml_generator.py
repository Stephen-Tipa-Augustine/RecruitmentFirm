#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import datetime

class AppendToXML:
    def __init__(self, xml_path=None, *arg, **kwargs):
        self.DOMTree = xml.dom.minidom.parse(xml_path)
        self.collection = self.DOMTree.documentElement
    def setText(self, doc, node, text):
        textnode = doc.createTextNode(text)
        node.appendChild(textnode)
    def createChild(self, name, email):
        now = datetime.datetime.now()
        date = now.strftime("%m/%d/%Y, %H:%M:%S")
        data = self.DOMTree.createElement('user')
        data.setAttribute('title', 'Job Seeker')
        sub_element1 = self.DOMTree.createElement('name')
        sub_element2 = self.DOMTree.createElement('email')
        sub_element3 = self.DOMTree.createElement('date')
        self.setText(self.DOMTree, sub_element1, name)
        self.setText(self.DOMTree, sub_element2, email)
        self.setText(self.DOMTree, sub_element3, date)
        data.appendChild(sub_element1)
        data.appendChild(sub_element2)
        data.appendChild(sub_element3)
        self.collection.appendChild(data)
    def saveToXML(self):
        with open("xml_path", 'w') as output:
         output.write(self.DOMTree.toprettyxml())