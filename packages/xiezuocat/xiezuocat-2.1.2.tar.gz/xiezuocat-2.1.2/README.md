# xiezuocat-python
对智能纠错、智能改写、AI写作、单点登录签名算法进行封装<br />
关于具体接口的调用方法与参数说明，请访问[写作猫API文档中心](https://apidocs.xiezuocat.com/guide/)
## 一、pip引入
```python
pip install xiezuocat
```

## 二、调用示例
### 1、智能纠错
#### 调用示例
```python
import xiezuocat
import json
my_xiezuocat = xiezuocat.Xiezuocat({your-secretKey})
check_data = json.dumps({
            "texts": [
                "河北省赵县的洨河上，有一座世界文明的石拱桥，叫安济桥，又叫赵州桥。",
                "它是隋朝的石匠李春涉及和参加建造的，到现在已经有一千三百多年了。"
            ]
        })
check_result = my_xiezuocat.check(check_data)
print(check_result)
```
#### 返回结果
```json
{
  "errCode" : 0,
  "errMsg" : "",
  "data" : null,
  "alerts" : [ [ {
    "alertType" : 4,
    "alertMessage" : "建议用“闻名”替换“文明”。",
    "sourceText" : "文明",
    "replaceText" : "闻名",
    "start" : 15,
    "end" : 16,
    "errorType" : 1,
    "advancedTip" : false
  } ], [ {
    "alertType" : 4,
    "alertMessage" : "建议用“设计”替换“涉及”。“涉及”指关联到，牵涉到。“设计”指根据一定要求﹐对某项工作预先制定图样﹑方案。",
    "sourceText" : "涉及",
    "replaceText" : "设计",
    "start" : 9,
    "end" : 10,
    "errorType" : 1,
    "advancedTip" : false
  } ] ],
  "checkLimitInfo" : {
    "checkWordCountLeftToday" : "996730",
    "totalCheckWordCountLeft" : "996730",
    "expireDate" : "2024-02-02 00:00:00"
  }
}
```
### 2、智能改写
##### 调用示例
```python
import xiezuocat
import json
my_xiezuocat = xiezuocat.Xiezuocat({your-secretKey})
rewrite_data = json.dumps({
  "items": [
    "河北省赵县的洨河上，有一座世界文明的石拱桥，叫安济桥，又叫赵州桥。它是隋朝的石匠李春涉及和参加建造的，到现在已经有一千三百多年了。"
  ],
  "level": "middle"
})
rewrite_result = my_xiezuocat.rewrite(rewrite_data)
print(rewrite_result)
```
##### 返回结果
```json
{
  "errcode" : 0,
  "errmsg" : null,
  "items" : [ "河北省赵县境内，有一座名为“安济桥”的“赵州桥”，是一座举世闻名的“世界文化遗产”。这座桥由李春参与修建，距今已有1300年之久。" ],
  "stat" : "996730"
}
```

### 3、AI写作
#### 创建生成任务
##### 调用示例
```python
import xiezuocat
import json
my_xiezuocat = xiezuocat.Xiezuocat({your-secretKey})
generate_params = json.dumps({
    "type": "Step",
    "title": "仿生人会梦见电子羊吗",
    "length": "default"
})
result = my_xiezuocat.generate(generate_params)
print(result)
```
##### 返回结果
```json
{
  "errCode" : 0,
  "errMsg" : "success",
  "data" : {
    "docId" : "36f72645-2bd3-43a3-85a3-0512e2d52cd3"
  }
}
```

#### 获取生成结果
##### 调用示例
```python
import xiezuocat
my_xiezuocat = xiezuocat.Xiezuocat({your-secretKey})
doc_id = "36f72645-2bd3-43a3-85a3-0512e2d52cd3" # 此处docId为第一步生成的结果
result = my_xiezuocat.get_generate_result(doc_id)
print(result)
```
##### 返回结果
```json
{
  "errCode" : 0,
  "errMsg" : "success",
  "data" : {
    "status" : "FINISHED",
    "result" : "仿生人会梦见电子羊吗\n仿生人，即为人工仿生系统，其本质上是利用计算机技术模拟人体生理机能，设计制造出一种与人类相似的人工生物，具有一定的智力、语言、动作等。其设计原理简单来讲就是通过模仿生物体自身的神经回路结构，模拟人工生物的大脑信号。在过去很长一段时间内，仿生人始终是科幻小说和影视作品中虚构出来的角色。随着科技进步不断发展，现实生活中也有了许多仿生人形象。比如：人类模仿机械动物造型、电子羊造型等等。今天我们就来聊聊这类仿生人形象的故事。\n一、人体仿生人\n随着科学技术的发展，仿生技术也在不断地创新，这其中最为典型的当属“人体仿生人”了。所谓的人体仿生人就是通过模仿人体形态特征、生理机能，设计制造出与真人一样的“机器人”。\n二、机械人\n机械人是利用计算机技术在人体上植入程序，进行人工模仿和设计。比如机器人手臂的关节都是有关节定位的，所以可以像人类手臂一样灵活地运动。这种仿生机器人最大的特点就是可以根据不同类型的动作进行相应的调节。目前机器人在军事领域应用最为广泛，比如：军事侦察、特种部队、无人机等等。\n三、电子羊\n电子羊，又名“仿生人”，是一种可以通过模拟生物行为而非机械结构来实现动作的计算机仿真机器人。电子羊具有很强的环境适应能力和自我保护能力，能够完成复杂任务，具备多种动作模式和智能控制机制。目前，国际上已有相关研究团队进行了研发，并应用于人类生活中。\n四、仿生人与智能机器人\n当前，我们可以通过人工仿生系统来实现机器人的多种功能，比如：帮助人类去完成某些任务、帮助机器人控制一些智能设备等。在这方面的应用已经取得了不少成果。比如：利用仿生人模型在机器人身上进行虚拟现实技术测试，为将来机器人开发提供新的思路，甚至还可以直接与仿生人对话。除此之外，还有一些应用在医疗方面，比如：利用仿生人模拟心脏功能来设计人工心脏，实现了人体自身对机械和物理机制的自我调节；利用仿生人设计出人造器官，可以帮助人类实现器官移植手术的顺利进行等等。未来随着科技进步和仿生人研究的深入，我们有望看到更多高智能、高水平的仿生人形象出现在我们眼中。\n",
    "wordCount" : "852",
    "restCount" : "90578"
  }
}
```
### 4、单点登录签名算法
##### 调用示例
```python
import xiezuocat
my_xiezuocat = xiezuocat.Xiezuocat({your-secretKey})
sign_result = my_xiezuocat.get_sso_signature({your-appId}, {your-uid})
print(sign_result)
```
##### 返回结果
```json
eydhcHBJZCc6ICd4eCcsICd1aWQnOiAnbGwnLCAndGltZXN0YW1wJzogMTY4MDUxMTExNy42NjIyMTc2LCAnc2lnbic6ICdmZTM2MmU4MzBkMTFlZDc3ZDkwZjhhNzk0NzkwM2RlMDY1ODA2NjY2NDEzMjg4ZGJjNzFmMzk5MjhmODBlOTAxJ30=
```
##### 拿到签名之后访问下述URL即可登录写作猫
```js
// p为签名算法生成的结果
https://xiezuocat.com/api/open/login?p=eydhcHBJZCc6ICd4eCcsICd1aWQnOiAnbGwnLCAndGltZXN0YW1wJzogMTY4MDUxMTExNy42NjIyMTc2LCAnc2lnbic6ICdmZTM2MmU4MzBkMTFlZDc3ZDkwZjhhNzk0NzkwM2RlMDY1ODA2NjY2NDEzMjg4ZGJjNzFmMzk5MjhmODBlOTAxJ30=
```