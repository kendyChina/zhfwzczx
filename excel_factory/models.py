from django.db import models

# Create your models here.

# coding: utf-8

# '="省分"', '="地市"', '="正式订单号"', '="ICCID"', '="订单时间"', '="订购号码"', '="客户姓名"',
# '="证件号码"', '="联系电话"', '="性别"', '="年龄"', '="订单状态"', '="套餐名称"', '="商品名称"',
# '="退单时间"', '="退单原因"', '="开户时间"', '="激活状态"', '="激活时间"', '="推广渠道编码"',
# '="推广渠道名称"', '="推广发展人编码"', '="推广发展人名称"', '="渠道编码"', '="渠道名称"',
# '="发展人编码"', '="发展人名称"', '="交付方式"', '="推荐人"', '="推广人ID"', '="码上购类别"',
# '="上线手机号"', '="收货地址"', '="开户发展渠道类型"', '="是否二次营销"'
class Xsg(models.Model):
    sf = models.CharField(max_length=100, null=True)
    ds = models.CharField(max_length=100, null=True)
    zsddh = models.CharField(primary_key=True, max_length=100)
    iccid = models.CharField(max_length=100, null=True)
    ddsj = models.CharField(max_length=100, null=True)
    ddrq = models.CharField(max_length=100, null=True)
    ddyf = models.CharField(max_length=100, null=True)
    dghm = models.CharField(max_length=100, null=True)
    khxm = models.CharField(max_length=100, null=True)
    zjhm = models.CharField(max_length=100, null=True)
    lxdh = models.CharField(max_length=100, null=True)
    xb = models.CharField(max_length=100, null=True)
    nl = models.CharField(max_length=100, null=True)
    ddzt = models.CharField(max_length=100, null=True)
    tcmc = models.CharField(max_length=100, null=True)
    spmc = models.CharField(max_length=100, null=True)
    tdsj = models.CharField(max_length=100, null=True)
    tdyy = models.CharField(max_length=100, null=True)
    khsj = models.CharField(max_length=100, null=True)
    jhzt = models.CharField(max_length=100, null=True)
    jhsj = models.CharField(max_length=100, null=True)
    jhrq = models.CharField(max_length=100, null=True)
    jhyf = models.CharField(max_length=100, null=True)
    tgqdbm = models.CharField(max_length=100, null=True)
    tgqdmc = models.CharField(max_length=100, null=True)
    tgfzrbm = models.CharField(max_length=100, null=True)
    tgfzrmc = models.CharField(max_length=100, null=True)
    qdbm = models.CharField(max_length=100, null=True)
    qdmc = models.CharField(max_length=100, null=True)
    fzrbm = models.CharField(max_length=100, null=True)
    fzrmc = models.CharField(max_length=100, null=True)
    jffs = models.CharField(max_length=100, null=True)
    tjr = models.CharField(max_length=100, null=True)
    tgrid = models.CharField(max_length=100, null=True)
    msglb = models.CharField(max_length=100, null=True)
    sxsjh = models.CharField(max_length=100, null=True)
    shdz = models.CharField(max_length=100, null=True)
    khfzqdlx = models.CharField(max_length=100, null=True)
    sfecyx = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.zsddh

# '内部订单号', '外部订单号', '外部下单时间', '生产模式', '订单来源', '商品类型', '商品名称', '开户号码',
# '地市', '环节', '支付时间', '支付流水号', '支付类型', '物流单号', '套餐名称', '首月资费方式', '是否异常单',
# '自动化异常类型', '自动化异常原因', '人工标记类型', '异常原因', '备注信息', '配送方式', '支付方式',
# '发展人名称', '发展人编码', '终端号', '卡串号', '品牌', '发票抬头', '推荐人姓名', '发货时间',
# '物流公司', '收货人姓名', '收货人电话', '买家留言', '卖家留言', '订单金额(元)', '开户时间', '商品数量',
# '支付状态', 'WMS退单状态', '签收状态', '回单状态', '是否预约单', '商品小类', '网别', '是否老用户',
# '收货人地址', '退单状态', '退单时间', '代金券编码', '代金券名称', '退款状态', '激活状态', '审核状态',
# '审核备注', '撤单状态', '签收时间', '首次配送失败时间', '激活时间', '退单原因', '证件照上传状态', '证件审核状态'
class Wyg(models.Model):
    dbddh = models.CharField(max_length=100, primary_key=True)
    wbddh = models.CharField(max_length=100, null=True)
    wbxdsj = models.CharField(max_length=100, null=True)
    wbxdrq = models.CharField(max_length=100, null=True)
    wbxdyf = models.CharField(max_length=100, null=True)
    scms = models.CharField(max_length=100, null=True)
    ddly = models.CharField(max_length=100, null=True)
    splx = models.CharField(max_length=100, null=True)
    spmc = models.CharField(max_length=100, null=True)
    khhm = models.CharField(max_length=100, null=True)
    ds = models.CharField(max_length=100, null=True)
    hj = models.CharField(max_length=100, null=True)
    zfsj = models.CharField(max_length=100, null=True)
    zflsh = models.CharField(max_length=100, null=True)
    zflx = models.CharField(max_length=100, null=True)
    wldh = models.CharField(max_length=100, null=True)
    tcmc = models.CharField(max_length=100, null=True)
    syzffs = models.CharField(max_length=100, null=True)
    sfycd = models.CharField(max_length=100, null=True)
    zdhyclx = models.CharField(max_length=100, null=True)
    zdhycyy = models.CharField(max_length=100, null=True)
    rgbjlx = models.CharField(max_length=100, null=True)
    ycyy = models.CharField(max_length=100, null=True)
    bzxx = models.CharField(max_length=100, null=True)
    psfs = models.CharField(max_length=100, null=True)
    zffs = models.CharField(max_length=100, null=True)
    fzrmc = models.CharField(max_length=100, null=True)
    fzrbm = models.CharField(max_length=100, null=True)
    zdh = models.CharField(max_length=100, null=True)
    kch = models.CharField(max_length=100, null=True)
    pp = models.CharField(max_length=100, null=True)
    fptt = models.CharField(max_length=100, null=True)
    tjrxm = models.CharField(max_length=100, null=True)
    fhsj = models.CharField(max_length=100, null=True)
    wlgs = models.CharField(max_length=100, null=True)
    shrxm = models.CharField(max_length=100, null=True)
    shrdh = models.CharField(max_length=100, null=True)
    mjly = models.CharField(max_length=100, null=True)
    mjly2 = models.CharField(max_length=100, null=True)
    ddje = models.CharField(max_length=100, null=True)
    khsj = models.CharField(max_length=100, null=True)
    spsl = models.CharField(max_length=100, null=True)
    zfzt = models.CharField(max_length=100, null=True)
    wmstdzt = models.CharField(max_length=100, null=True)
    qszt = models.CharField(max_length=100, null=True)
    hdzt = models.CharField(max_length=100, null=True)
    sfyyd = models.CharField(max_length=100, null=True)
    spxl = models.CharField(max_length=100, null=True)
    wb = models.CharField(max_length=100, null=True)
    sflyh = models.CharField(max_length=100, null=True)
    shrdz = models.CharField(max_length=100, null=True)
    tdzt = models.CharField(max_length=100, null=True)
    tdsj = models.CharField(max_length=100, null=True)
    djqbm = models.CharField(max_length=100, null=True)
    djqmc = models.CharField(max_length=100, null=True)
    tkzt = models.CharField(max_length=100, null=True)
    jhzt = models.CharField(max_length=100, null=True)
    shzt = models.CharField(max_length=100, null=True)
    shbz = models.CharField(max_length=100, null=True)
    cdzt = models.CharField(max_length=100, null=True)
    qssj = models.CharField(max_length=100, null=True)
    scpssbsj = models.CharField(max_length=100, null=True)
    jhsj = models.CharField(max_length=100, null=True)
    jhrq = models.CharField(max_length=100, null=True)
    jhyf = models.CharField(max_length=100, null=True)
    tdyy = models.CharField(max_length=100, null=True)
    zjzsczt = models.CharField(max_length=100, null=True)
    zjshzt = models.CharField(max_length=100, null=True)

# '用户编号', '电话号码', '发展部门', '入网时间', '入网月份', '状态', '产品编码',
# '产品名称', '余额', '最后停机时间', '首次充值金额', '首次充值时间',
# '累计充值金额', '是否充值', '发展区域', 'CBSS发展人'
class Cz(models.Model):
    yhbh = models.CharField(max_length=100, primary_key=True)
    dhhm = models.CharField(max_length=100, null=True)
    fzbm = models.CharField(max_length=100, null=True)
    rwsj = models.CharField(max_length=100, null=True)
    jhrq = models.CharField(max_length=100, null=True)
    jhyf = models.CharField(max_length=100, null=True)
    rwyf = models.CharField(max_length=100, null=True)
    zt = models.CharField(max_length=100, null=True)
    cpbm = models.CharField(max_length=100, null=True)
    cpmc = models.CharField(max_length=100, null=True)
    ye = models.CharField(max_length=100, null=True)
    zhtjsj = models.CharField(max_length=100, null=True)
    scczje = models.CharField(max_length=100, null=True)
    scczsj = models.CharField(max_length=100, null=True)
    scczrq = models.CharField(max_length=100, null=True)
    scczyf = models.CharField(max_length=100, null=True)
    ljczje = models.CharField(max_length=100, null=True)
    sfcz = models.CharField(max_length=100, null=True)
    fzqy = models.CharField(max_length=100, null=True)
    cbssfzr = models.CharField(max_length=100, null=True)

# 项目
class Xm(models.Model):
    def __str__(self):
        return "%s：%s" % (self.xm, self.fzrbm)

    fzrbm = models.CharField(max_length=100, primary_key=True)
    xm = models.CharField(max_length=100, null=True)

# '订单号', '订单ID', 'ESS订单号', '订单日期', '订单状态', '省分', '地市', '商品类型', '商品名称',
# '套餐名称', '订购号码', '终端品牌', '终端型号', '终端颜色', '活动类型', '可选包', '商城实收',
# '支付状态', '支付方式', '客户姓名', '证件类型', '证件号码', '联系人', '联系人电话', '其他联系人电话',
# '配送地址', '客户备注', '权益类型', '权益明细', '发展人姓名', '发展人编码', '归属渠道', '渠道来源',
# '用户类型', '实名制激活状态', '换卡激活状态'
class Ddcx(models.Model):
    def __str__(self):
        return self.ddh

    ddh = models.CharField(max_length=100, primary_key=True)
    ddid = models.CharField(max_length=100, null=True)
    essddh = models.CharField(max_length=100, null=True)
    ddrq = models.CharField(max_length=100, null=True)
    ddrq2 = models.CharField(max_length=100, null=True)
    ddyf = models.CharField(max_length=100, null=True)
    ddzt = models.CharField(max_length=100, null=True)
    sf = models.CharField(max_length=100, null=True)
    ds = models.CharField(max_length=100, null=True)
    splx = models.CharField(max_length=100, null=True)
    spmc = models.CharField(max_length=100, null=True)
    tcmc = models.CharField(max_length=100, null=True)
    dghm = models.CharField(max_length=100, null=True)
    zdpp = models.CharField(max_length=100, null=True)
    zdxh = models.CharField(max_length=100, null=True)
    zdys = models.CharField(max_length=100, null=True)
    hdlx = models.CharField(max_length=100, null=True)
    kxb = models.CharField(max_length=100, null=True)
    scss = models.CharField(max_length=100, null=True)
    zfzt = models.CharField(max_length=100, null=True)
    zffs = models.CharField(max_length=100, null=True)
    khxm = models.CharField(max_length=100, null=True)
    zjlx = models.CharField(max_length=100, null=True)
    zjhm = models.CharField(max_length=100, null=True)
    lxr = models.CharField(max_length=100, null=True)
    lxrdh = models.CharField(max_length=100, null=True)
    qtlxrdh = models.CharField(max_length=100, null=True)
    psdz = models.CharField(max_length=100, null=True)
    khbz = models.CharField(max_length=100, null=True)
    qylx = models.CharField(max_length=100, null=True)
    qymx = models.CharField(max_length=100, null=True)
    fzrxm = models.CharField(max_length=100, null=True)
    fzrbm = models.CharField(max_length=100, null=True)
    gsqd = models.CharField(max_length=100, null=True)
    qdly = models.CharField(max_length=100, null=True)
    yhlx = models.CharField(max_length=100, null=True)
    smzjhzt = models.CharField(max_length=100, null=True)
    hkjhzt = models.CharField(max_length=100, null=True)

