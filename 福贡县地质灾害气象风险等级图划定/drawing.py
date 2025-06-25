def picture_drawing(colors):
    import matplotlib
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.io.shapereader as shpreader
    import matplotlib.patches as mpatches

    fig = plt.figure(figsize=(12,8))

    # 设置字体为 SimHei
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    """投影方式：可丽投影"""
    crs = ccrs.PlateCarree()

    ax = fig.add_subplot(111,projection=crs)

    """范围设置"""
    start_lon = 98.5  #开始经度（西）
    end_lon = 99.22    #结束经度（东）
    start_lat = 26.3  #开始纬度（南）
    end_lat = 27.7   #结束纬度（北）
    extend = [start_lon,end_lon,start_lat,end_lat]
    ax.set_extent(extend, crs)

    xiangs = []

    filepath = '福贡/架科底/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    jiakedi = reader.geometries()
    xiangs.append(jiakedi)

    filepath = '福贡/鹿马登/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    lumaddeng = reader.geometries()
    xiangs.append(lumaddeng)

    filepath = '福贡/马吉/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    maji = reader.geometries()
    xiangs.append(maji)

    filepath = '福贡/匹河/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    pihe = reader.geometries()
    xiangs.append(pihe)

    filepath = '福贡/上帕/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    shangpa = reader.geometries()
    xiangs.append(shangpa)

    filepath = '福贡/石月亮/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    shiyueliang = reader.geometries()
    xiangs.append(shiyueliang)

    filepath = '福贡/子里甲/POLYGON.shp'
    reader = shpreader.Reader(filepath)
    zilijia = reader.geometries()
    xiangs.append(zilijia)

    #各乡镇名称的标记
    towns = [
        {'name':'马吉','lon':98.79,'lat':27.398},
        {'name':'石月亮','lon':98.808,'lat':27.217},
        {'name':'鹿马登','lon':98.805,'lat':27.034},
        {'name':'上帕','lon':98.83,'lat':26.9},
        {'name':'架科底','lon':98.895,'lat':26.786},
        {'name':'子里甲','lon':98.90,'lat':26.69},
        {'name':'匹河','lon':98.90,'lat':26.53},
    ]
    for town in towns:
        ax.plot(town['lon'], town['lat'], 'ro', markersize=0, transform=ccrs.PlateCarree())
        ax.text(town['lon'],town['lat'], town['name'],
                transform=ccrs.PlateCarree(),
                fontsize=12, color='black')

    #于地图上添加各乡镇地图
    """
    for xiang in xiangs:
        ax.add_geometries(xiang,crs,lw = 0.5,fc = 'none')
    """

    ax.add_geometries(maji,crs,ec = 'black',fc = colors[0],lw = 1,alpha = 0.8)
    ax.add_geometries(shiyueliang,crs,ec = 'black',fc = colors[1],lw = 1,alpha = 0.8)
    ax.add_geometries(lumaddeng,crs,ec = 'black',lw = 1,fc = colors[2],alpha = 0.8)
    ax.add_geometries(shangpa,crs,ec = 'black',lw = 1,fc = colors[3],alpha = 0.8)
    ax.add_geometries(jiakedi,crs,ec = 'black',lw = 1,fc = colors[4],alpha = 0.8)
    ax.add_geometries(zilijia,crs,ec = 'black',lw = 1,fc = colors[5],alpha = 0.8)
    ax.add_geometries(pihe,crs,ec = 'black',lw = 1,fc = colors[6],alpha = 0.8)

    # 创建分类图例
    legend_elements = [
        mpatches.Patch(facecolor='red', edgecolor='black', label='I级（风险很高）'),
        mpatches.Patch(facecolor='orange', edgecolor='black', label='II级（风险高）'),
        mpatches.Patch(facecolor='yellow', edgecolor='black', label='III级（风险较高）')
    ]

    ax.legend(handles=legend_elements, loc='upper right')

    ax.set_title('福贡县地质灾害气象风险等级图',fontsize = 20)

    #ax.text(0.12,0.07,'福贡县气象台2025年5月19日18时发布',transform=ax.transAxes)

    reader.close()
    plt.savefig('my_plot.png',bbox_inches='tight')
    plt.show()