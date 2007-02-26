#! /usr/bin/python
# -*- Python -*-

import sys
sys.path.insert(0, '../pyalsa')
del sys
import alsahcontrol

def info(element):
	info = alsahcontrol.Info(element)
	enumerated = alsahcontrol.ElementType['Enumerated']
	integer = alsahcontrol.ElementType['Integer']
	integer64 = alsahcontrol.ElementType['Integer64']
	for a in dir(info):
		if a.startswith('__'):
			continue
		if a in ['items', 'itemNames'] and info.type != enumerated:
			continue
		if a in ['min', 'max', 'step'] and info.type != integer:
			continue
		if a in ['min64', 'max64', 'step64'] and info.type != integer64:
			continue
		extra = ''
		if a == 'type':
			extra = ' (%s)' % alsahcontrol.ElementTypeName[info.type]
		print '  %s: %s%s' % (a, getattr(info, a), extra)

def value(element):
	info = alsahcontrol.Info(element)
	value = alsahcontrol.Value(element)
	for a in dir(value):
		if a.startswith('__'):
			continue
		print '  %s: %s' % (a, getattr(value, a))
	values = value.getTuple(info.type, info.count)
	print '  Values: ', values
	value.setTuple(info.type, values)
	value.read()
	if info.isWritable:
		value.write()

print 'InterfaceId:'
print '  ', alsahcontrol.InterfaceId
print 'InterfaceName:'
print '  ', alsahcontrol.InterfaceName
print 'ElementType:'
print '  ', alsahcontrol.ElementType
print 'ElementTypeName:'
print '  ', alsahcontrol.ElementTypeName
print 'EventClass:'
print '  ', alsahcontrol.EventClass
print 'EventMask:'
print '  ', alsahcontrol.EventMask
print 'EventMaskRemove:', alsahcontrol.EventMaskRemove
print '  ', alsahcontrol.OpenMode
print 'EventMaskRemove:', alsahcontrol.OpenMode

hctl = alsahcontrol.HControl()
print 'Count: ', hctl.count
list = hctl.list()
print 'List:'
print list
for l in list:
	print '*****'
	element1 = alsahcontrol.Element(hctl, l[1:])
	info(element1)
	print '-----'
	value(element1)
del hctl