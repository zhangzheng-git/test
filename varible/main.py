# def testfunc(var1, var2):
#     var1 += a
#     var2 += 3
#
#     return var1, var2
#
#
# if __name__ == '__main__':
#     a = 4
#     b = 7
#     x,y = testfunc(var1=2,var2=8)
#     print(x,y)



from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("bar_toolbox.html")
)