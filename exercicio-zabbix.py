from pyzabbix import ZabbixAPI

zbx = ZabbixAPI('http://drone.rj2.alog.com.br/zabbix/')
zbx.login('zabbix', 'zabbix')
#print(zbx.api_version())

ret = zbx.host.get(
    output="host",
    selectGroups=True,
    selectInterfaces=True
)

for i in ret:
    print(i['interfaces'])

periodo = {
    "timeperiod_type": 3,
    "dayofweek": 64,
    "start_time": 64800,
    "period": 3600
}

ret = zbx.maintenance.create(
    name='Sardinha Boladao3',
    active_since='1558717964',
    active_till='1558747964',
    groupids=[12],
    timeperiods=[periodo]
)

print(ret)







from pyzabbix import ZabbixAPI

zbx = ZabbixAPI('http://drone.rj2.alog.com.br/zabbix/')
zbx.login('zabbix', 'zabbix')

ret = zbx.hostgroup.create(
    name='Hostgroup do Marco - Oreia'
)

interface = {
    "type": 1,
    "main": 1,
    "useip": 1,
    "ip": '8.8.8.8',
    "dns": "",
    "port": 10050
}
zbx.host.create(
    host='Lulinha2',
    interfaces=[interface],
    groups=[
        {
            "groupid": 12
        }
    ],

)