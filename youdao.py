# -*- coding: utf-8 -*-
__author__ = 'kingdee'
import httplib;
import json;
en = raw_input("请输入要查询的英语（逗号分隔）：");
ens = en.split(",");
youdao = httplib.HTTPConnection(host='dict.youdao.com');
for e in ens:
    word=[];
    youdao.request(method="GET",url="/jsonapi?q="+e+"&keyfrom=deskdict.suggest&dogVersion=1.0&dogui=json&client=deskdict&id=1847079e1fb1589fc&vendor=alading&in=YoudaoDict_6.3.69.4001_alading.1460712704&appVer=6.3.69.8341&appZengqiang=0&abTest=5&le=eng&dicts={\"count\":11,\"dicts\":[[\"ec\",\"ee\"],[\"collins\"],[\"phrs\",\"syno\",\"rel_word\"],[\"auth_sents_part\"],[\"web_search\"],[\"typos\"],[\"collins_part\"]]}&LTH=78");
    resp = youdao.getresponse();
    content = resp.read();
    jsonobj = json.loads(content);
    #
    word.append(e);
    if "ec" in jsonobj:
        w1 = jsonobj["ec"]["word"][0];
        if "usphone" in w1:
            word.append(w1["usphone"]);
        else:
            word.append(w1["phone"]);

        ecword = jsonobj["ec"]["word"][0];
        if "wfs" in ecword:
            wfs = ecword["wfs"];
            if wfs:
                state = '';
                for wf in wfs:
                    state = state + wf["wf"]["name"]+":"+wf["wf"]["value"] + ","
                word.append(state);
        if "trs" in ecword:
            trs = ecword["trs"];
            if trs:
                for tr in trs:
                    word.append(tr["tr"][0]["l"]["i"][0]);
        ee = jsonobj["ee"]["word"]["trs"];
        if ee:
            for tr in ee:
                trss = tr["pos"]+" ";
                etr = tr["tr"];
                for t in etr:
                    word.append(trss + t["l"]["i"]);
                    if "similar-words" in t:
                        word.append(json.dumps(t["similar-words"]).replace("[","").replace("]","").replace("{","").replace("}",""));
        for v in word:
            print(v);
        print("-----------------你好，我是分割线-----------------");
        resp.close();
youdao.close();