# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:56:17 2022

@author: edlaptop
"""
update_note = { 
"top0": "内测会员账户已开放, 欢迎提交申请(http://www.topfintech.org/user_management); 提交bug报告,送永久免费数据使用权限",
"top1": "API数据接口用户手册PDF文档已开放下载:http://www.topfintech.org/TF_API",
"top2": "邀请内测用户加wx群讨论问题： wx: dredw_tf (加好友请备注账户名)",
"top3": '用户验证流程已优化, 现只需要提供访问密匙就可在客户端登录服务器, 旧用户请在微信公众号输入"重置密匙"获取访问密匙',
"v0.5.4": "开放国债逆回购tick数据, 开放gen_tdlist函数, 用于返回指定A股交易日集合",
"v0.5.0": "优化hf_min数据获取方法,现可选1-60min freq, 重新整理get_daily接口, 将数据分为daily,valuation,ms三大类,将HSGT设为独立接口,详见最新说明文档",
"v0.4.0": "加入事件学习,策略回测功能",
"v0.3.1": "优化用户验证方式,客户端不再需要安装加密库以便兼容用户在其他量化平台使用客户端, 现采用动态访问密匙,而不再需要用户名+密码, 用户信息加密由服务器处理",
"v0.2.9": "日间分钟线(股票, ETF) 可选择 1,3,5,10,15,30分钟频率数据, 详见 说明文本, self.hf_min",
"v0.2.8": "日间分钟线(股票, ETF) 数据开放, 详见 说明文本, self.hf_min",
"v0.2.7": "hot fix self.get_daily 错误",
"v0.2.6": "ETF期权表单get_1d数据标签，修正get_daily pindex 错误问题",
"v0.2.5": "添加可转债日线、扩展日线，tick，hf5数据接口，添加上交所股指期权日线、扩展日线，tick、hf5数据接口",
"v0.2.4": "添加一系列可转债get_1d 数据标签",
"v0.2.2": "get_daily 前后中复权选项， 微信公众号可申请会员账号",
"v0.2.0": "get_1d表单数据接口新att: delisted_date_A,ST_stock_A,SST_stock_A。",
"v0.1.9": "开放tick数据(get_tick),五档行情数据(get_hf5)接口, 扩展日线数据接口开放大小单资金流、不可回测系估价日线指标, 优化说明文档提取接口。 ",
"v0.1.8": "离线读取说明文档",
"v0.1.7": "更新1d数据接口标签: BJA北交所股票名单,stocklisting_SHSZ 不含北交所的正常交易A股名单。",
"v0.1.6": "减少常用日线接口(get_daily)在缺失日期参数情况下返回的数据时间段至近三个交易日。",
}