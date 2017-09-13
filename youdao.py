# -*- coding: utf-8 -*-
__author__ = 'kingdee'
import httplib;
import json;
en = raw_input("请输入要查询的英语（逗号分隔）：");
ens = en.split(",");
youdao = httplib.HTTPConnection(host='dict.youdao.com');
for e in ens:
    word=[];
    youdao.request(method="GET",url="/jsonapi?q="+e+"&keyfrom=deskdict.suggest&dogVersion=1.0&dogui=json&client=deskdict&id=1847079e1fb1589fc&vendor=alading&in=YoudaoDict_6.3.69.4001_alading.1460712704&appVer=6.3.69.8341&appZengqiang=0&abTest=5&le=eng&dicts={\"count\":11,\"dicts\":[[\"ec\"],[\"collins\"],[\"phrs\",\"syno\",\"rel_word\"],[\"auth_sents_part\"],[\"web_search\"],[\"typos\"],[\"collins_part\"]]}&LTH=78");
    resp = youdao.getresponse();
    content = resp.read();
    jsonobj = json.loads(content);
    #
    word.append(e+"\n");
    word.append(jsonobj["ec"]["word"][0]["usphone"]);
    vgq = jsonobj["ec"]["word"][0]["wfs"];
    if vgq:
        for wfs in vgq:
            word.append(wfs["wf"]["name"]+":"+wfs["wf"]["value"]);
    print(json.dumps(word,encoding="utf-8", ensure_ascii=False, sort_keys=True));
    resp.close();
youdao.close();