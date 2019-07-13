from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from excel_factory.models import Xsg, Wyg, Cz
from django.db.utils import IntegrityError
from django.conf import settings
from django.db import connection
import csv, os, datetime



# Create your views here.

# coding: utf-8

def remove_quo(str):
    return str.strip("=").strip('"')

def replace(str):
    return str.replace("\n", "")

class Insert():

    def __init__(self, file, header, model, header_line=1, get_date=[], batch_size = 20):
        self.file = file # 文件
        self.header_line = int(header_line) # 表头所在行数
        self.header = list(map(remove_quo, header)) # 表头名称
        self.model = model # 数据库
        self.get_date = get_date
        self.batch_size = batch_size
        self.batch = []
        self.succ_count = 0

    def __str__(self):
        return self.model

    def __save_file(self):
        self.local_file = os.path.join(settings.MEDIA_ROOT, self.file.name)
        with open(self.local_file, "wb") as f:
            for fc in self.file.chunks():
                f.write(fc)

    # 获取数据库字段
    def __get_header_key(self):
        self.header_key = []
        for f in self.model._meta.fields:
            self.header_key.append(f.get_attname())

    # 插入日期、月份
    def __insert_date(self):
        self.get_date.sort() # 从小到大排序
        countA = 1
        countB = 0
        for l in self.get_date:
            self.row.insert(l+countA, self.row[l+countB][:10]) # 增加日期
            countA += 1
            self.row.insert(l+countA, self.row[l+countB][:7])  # 增加日期
            countA += 1
            countB += 2

    def __get_models_dict(self):
        models_dict = {}
        ind = 0
        value = 0
        for h in self.header_key:
            ind = self.header_key.index(h)
            try:
                value = self.row[ind]
            except IndexError as e:
                value = None
                # print("IndexError in __get_models_dict")
                # exit(1)
            models_dict[h] = value

        self.batch.append(self.model(**models_dict))
        self.batch_now += 1

    def __bulk_create(self):
        self.model.objects.bulk_create(self.batch, ignore_conflicts=True)
        self.succ_count += self.batch_now
        self.batch_now = 0
        self.batch = []
        print("已录入%s行！" % self.succ_count)

    def run(self):

        self.__get_header_key()

        self.__save_file()

        self.batch_now = 0

        file_extension = os.path.splitext(self.local_file)[1]
        with open(self.local_file) as f:
            if file_extension == ".csv":
                with open(self.local_file) as f:
                    reader = csv.reader(f)
                    i = 1
                    while True:
                        header = list(map(remove_quo, next(reader)))
                        if i < self.header_line:
                            i += 1
                        else:
                            break

                    # 判断表头一致性
                    if self.header != header:
                        print("表头有变！")
                        print(self.header)
                        print(header)
                        return 1
                    else:
                        print("表头一致！")

                    for self.row in reader:
                        self.row = list(map(remove_quo, self.row))
                        self.__insert_date()

                        # self.batch_now + 1
                        self.__get_models_dict()
    
                        if self.batch_now < self.batch_size:
                            continue
                        try:
                            self.__bulk_create()
                        except BaseException as e:
                            print(e)
            elif file_extension == ".txt":
                # 把cbss发展人是None的都删掉，以免影响插入
                self.model.objects.filter(cbzzfzr=None).delete()

                i = 1
                while True:
                    header = next(f).strip("\n").split("\t")
                    if i < self.header_line:
                        i += 1
                    else:
                        break

                # 判断表头一致性
                if self.header != header:
                    print(self.header)
                    print(header)
                    print("表头有变！")
                    return 1
                else:
                    print("表头一致！")

                for self.row in f:
                    self.row = self.row.strip().split("\t")
                    self.__insert_date()

                    # self.batch_now + 1
                    self.__get_models_dict()

                    if self.batch_now < self.batch_size:
                        continue
                    try:
                        self.__bulk_create()
                    except BaseException as e:
                        print(e)
        os.remove(self.local_file)

def get_index(list, *args):
    result = []
    for arg in args:
        result.append(list.index(arg))
    return result


# 重定向index页
def index_redirect(request):
    return HttpResponseRedirect("index")

# index页
def index(request):
    return render(request, "excel_factory/index.html")

# 插入Xsg
def insert_xsg(request):
    if request.method == "GET":
        return render(request, "excel_factory/insert_xsg.html")
    header = ['="省分"', '="地市"', '="正式订单号"', '="ICCID"', '="订单时间"', '="订购号码"', '="客户姓名"',
              '="证件号码"', '="联系电话"', '="性别"', '="年龄"', '="订单状态"', '="套餐名称"', '="商品名称"',
              '="退单时间"', '="退单原因"', '="开户时间"', '="激活状态"', '="激活时间"', '="推广渠道编码"',
              '="推广渠道名称"', '="推广发展人编码"', '="推广发展人名称"', '="渠道编码"', '="渠道名称"',
              '="发展人编码"', '="发展人名称"', '="交付方式"', '="推荐人"', '="推广人ID"', '="码上购类别"',
              '="上线手机号"', '="收货地址"', '="开户发展渠道类型"', '="是否二次营销"']

    xsg = Insert(
        file=request.FILES.get("xsg"),
        header_line=int(request.POST.get("header_line")),
        header=header,
        model=Xsg,
        get_date=get_index(header, "订单时间", "激活时间")
    )
    xsg.run()

    return HttpResponse(u"上传成功！")

# 插入Wyg
def insert_wyg(request):
    if request.method == "GET":
        return render(request, "excel_factory/insert_wyg.html")
    header = ['内部订单号', '外部订单号', '外部下单时间', '生产模式', '订单来源', '商品类型', '商品名称', '开户号码',
              '地市', '环节', '支付时间', '支付流水号', '支付类型', '物流单号', '套餐名称', '首月资费方式', '是否异常单',
              '自动化异常类型', '自动化异常原因', '人工标记类型', '异常原因', '备注信息', '配送方式', '支付方式',
              '发展人名称', '发展人编码', '终端号', '卡串号', '品牌', '发票抬头', '推荐人姓名', '发货时间',
              '物流公司', '收货人姓名', '收货人电话', '买家留言', '卖家留言', '订单金额(元)', '开户时间', '商品数量',
              '支付状态', 'WMS退单状态', '签收状态', '回单状态', '是否预约单', '商品小类', '网别', '是否老用户',
              '收货人地址', '退单状态', '退单时间', '代金券编码', '代金券名称', '退款状态', '激活状态', '审核状态',
              '审核备注', '撤单状态', '签收时间', '首次配送失败时间', '激活时间', '退单原因', '证件照上传状态', '证件审核状态']

    wyg = Insert(
        file=request.FILES.get("wyg"),
        header_line=request.POST.get("header_line"),
        header=header,
        model=Wyg,
        get_date=get_index(header, "外部下单时间", "激活时间")
    )
    wyg.run()

    return HttpResponse(u"上传成功！")

# 插入Cz
def insert_cz(request):
    if request.method == "GET":
        return render(request, "excel_factory/insert_cz.html")
    header = ['用户编号', '电话号码', '发展部门', '入网时间', '入网月份', '状态',
              '产品编码', '产品名称', '余额', '最后停机时间', '首次充值金额', '首次充值时间',
              '累计充值金额', '是否充值', '发展区域', 'CBSS发展人']
    cz = Insert(
        file=request.FILES.get("cz"),
        header_line=request.POST.get("header_line"),
        header=header,
        model=Cz,
        get_date=get_index(header, "首次充值时间")
    )
    cz.run()

    return HttpResponse(u"HH")

def get_all_date(date_start, date_end):
    ds = datetime.datetime.strptime(date_start, "%Y-%m-%d")
    de = datetime.datetime.strptime(date_end, "%Y-%m-%d")
    dates = []

    while ds <= de:
        dates.append(ds.strftime("%Y-%m-%d"))
        ds += datetime.timedelta(days=1)

    return dates

def search_xsg(request):
    if request.method == "GET":
        return render(request, "excel_factory/search_xsg.html")
    fzrbm = request.POST.get("fzrbm")
    date_start = request.POST.get("date_start")
    date_end = request.POST.get("date_end")

    dates = get_all_date(date_start, date_end)

    with connection.cursor() as c:
        c.execute("""
            SELECT * FROM xsg_cz_xm WHERE xsg_cz_xm.推广发展人编码=%s
        """, (fzrbm, ))
        result = c.fetchall()

    table = [["订单日期", "订单量", "激活量", "激活率", "首充≥50", "充值率", "综转率"], ]

    # 统计订单量
    def count_ddl(date):
        i = 0
        for row in result:
            if row[7] == date:  # 判断订单日期
                i += 1
        return i

        # 统计激活量
    def count_jhl(date):
        i = 0
        for row in result:
            if row[7] == date and row[9] == "已激活":  # 判断订单日期和激活状态
                i += 1
        return i

    # 统计充值量
    def count_czl(date):
        i = 0
        for row in result:
            if row[13] is not None:
                if len(row[13]) > 0:
                    if row[7] == date and float(row[13]) >= 50:  # 判断订单日期和首充金额≥50
                        i += 1
        return i

    for date in dates:
        a = count_ddl(date)
        b = count_jhl(date)
        d = count_czl(date)

        if a == 0:
            c = "0.00%"
            f = "0.00%"
        else:
            c = "{:.2%}".format(b / a)  # 激活率
            f = "{:.2%}".format(d / a)  # 综转率
        if b == 0:
            e = "0.00%"
        else:
            e = "{:.2%}".format(d / b)  # 充值率

        row = [date, a, b, c, d, e, f]
        table.append(row)
    return render(request, "excel_factory/show_xsg.html", {"table": table})