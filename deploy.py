print '***************************'
connect('weblogic','weblogic1','t3://localhost:7001')
print '***************************'
edit()
print '***************************'
startEdit()
print '***************************'
deploy('Calendar','D:\Office\Installer\Calendar.war',targets="AdminServer")
print '***************************'
print '***************************'
activate()
print '***************************'
print 'For more script Please visit  www.sstechnicaltraining.com'
print 'We provide Weblogic Online and classroom training'
print 'Contact us at 09019655686'
disconnect()