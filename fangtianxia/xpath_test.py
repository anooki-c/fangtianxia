import scrapy
from scrapy.selector import Selector

content = '''

<!DOCTYPE html>
<html>
<head>
    <title>华侨城·欢乐天际基本信息,售楼处电话,物业费,物业电话,开发商-武汉房天下</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="renderer" content="webkit" />
    <link rel="dns-prefetch" href="//cdnsfb.soufunimg.com" />
    <link rel="dns-prefetch" href="//esf.js.soufunimg.com" />
    <link rel="dns-prefetch" href="//img1n.soufunimg.com" />
    <link rel="dns-prefetch" href="//img11.soufunimg.com" />
    <link rel="dns-prefetch" href="//js.ub.fang.com" />
    <link rel="dns-prefetch" href="//clickn.fang.com" />
    <link rel="dns-prefetch" href="//countubn.3g.fang.com" />
    <link rel="dns-prefetch" href="//countpvn.light.fang.com" />
    <link rel="dns-prefetch" href="//www.google-analytics.com" />
    <meta name="mobile-agent" content="format=html5;url=https://m.fang.com/xf/wuhan/2610156494/housedetail.html">
    <link rel="alternate" media="only screen and(max-width:640px)" href="https://m.fang.com/xf/wuhan/2610156494/housedetail.html">
    <meta name="keywords" content="华侨城·欢乐天际售楼处地址,华侨城·欢乐天际售楼电话,华侨城·欢乐天际物业费电话,华侨城·欢乐天际开发商" />
    <meta name="Description" content="武汉房天下为您提供华侨城·欢乐天际基本信息，包括售楼处地址，售楼电话，物业费，物业电话，开发商等华侨城·欢乐天际楼盘相关信息，为您选房、买房提供参考!" />
    <meta http-equiv="Content-Language" content="zh-cn" />
    <meta name="applicable-device" content="pc">
    <script type="text/javascript" src="//static.soufunimg.com/esf/clickfang/fangclick.min.js"></script>
    <script src="//static.soufunimg.com/common_m/pc_public/fangjs/build/ie8/ie8.2.js"  type="text/javascript"></script>
    
	<link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/housevilla_xfxiangqing.css?v=202109160001" rel="stylesheet"/>
    <link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/common/sfpc_base.css?v=202109160001" rel="stylesheet"/>


    <div id="dsy_D02_16"><div class="bigbanner" id="xmlAd" style='overflow:hidden;min-width: 1200px;'></div></div>
    
    <script type="text/javascript"
        src="//static.soufunimg.com/common_m/pc_public/fangjs/build/ie8/ie8.js?v=202109160001">
    </script>
    <script type="text/javascript" src="//static.soufunimg.com/common_m/pc_public/fangjs/build/imgerr/imgerr.js">
    </script>
    <script type="text/javascript"
        src="//static.soufunimg.com/common_m/pc_public/fangjs/build/??fang2.3.2.js,jquery/jquery-3.js?v=202109160001">
    </script>
    
    <script>
        var pageConfig = pageConfig || {};
        fang.config({
            base: '//static.soufunimg.com/esf/esf/online/loupannew/static/js/',
            ver: /test/.test(pageConfig.public) ? Math.random().toString(32).substring(2) :
                '202109160001'
        });
    </script>   
</head>
<body>
    
    <script type="text/javascript">
// uv
    var _dctc = _dctc || {};
    _dctc._account = _dctc._account || ['UA-24140496-1','UA-24829808-1','UA-24830538-1','UA-24829808-24','UA-24830538-24']
    _dctc.isNorth = _dctc.isNorth || 'N';
    _dctc.bid = '202024';
    try {
        if (_pageid) {
            _dctc.pageid = _pageid;
        }
    }
    catch (e) {
    }
    _dctc.page = 'xf_lp^xq_pc';
    _dctc.city = '武汉';
    _dctc.business = 'N';
</script>
<script type="text/javascript" src="//js.soufunimg.com/count/uvbforpc.js"></script>
<script>
    //ub
    _ub.city = '武汉';
    _ub.biz = 'n';
    _ub.location = '1';

    var ubb = 0;
    var ubp = {"vwg.page":"xf_lp^xq_pc","vwn.projectid":"2610156494","vwg.CreatingCity":"武汉"};
    if(ubb > -1 && ubp != null && JSON.stringify(ubp) != "{}")
    {
        _ub.collect(ubb,ubp);
    }
</script>



<link href="//static.soufunimg.com/navigation/style/navigation20141112.css?v=" rel="stylesheet" type="text/css"/>
<link
href="//static.soufunimg.com/homepage/new/family/css/navsupply.css?v=" rel="stylesheet" type="text/css"/>
<!-- 导航begin -->
<div class="newnav20141104" source='navnode'>
	<div class="newnav20141104nr">
		<input
		type="hidden" id="channelDsy" name="channelDsy" value="newhouse"><div class="s1">
			<a href="https://www.fang.com/"><img alt="" src="//static.soufunimg.com/navigation/images/navlogo.gif"></a>
		</div>
			<div class="s2" onmouseover="this.className='s2 on2014'" onmouseout="this.className='s2'" id="dsy_H01_01">
				<div class="s4Box">
					<a href="#">武汉</a>
					<img src="//static.soufunimg.com/navigation/images/navicon.gif">
					
				</div>
				
						<div class="city20141104">
                  <!--city_list_start-->
                <!--tab_header_start-->

				<div class="city20141104hd">

					<div class="city1">热门城市</div>

					<div class="city2">ABCDFGH</div>

					<div class="city2">JKLMNQST</div>

					<div class="city2">WXYZ</div>

                    <!--more_tab-->
			    </div>

            	<!--tab_header_end-->

				<div class="city20141104nr" id="cityi010" style="display: block;">
                <!--tab1_content_start-->
                    	<a target="_self" href="https://newhouse.fang.com">全国</a>
                    	<a target="_self" href="https://newhouse.fang.com">北京</a>
						<a target="_self" href="https://sh.newhouse.fang.com">上海</a>
						<a target="_self" href="https://gz.newhouse.fang.com">广州</a>
						<a target="_self" href="https://sz.newhouse.fang.com">深圳</a>
						<a target="_self" href="https://cd.newhouse.fang.com">成都</a>
						<a target="_self" href="https://cq.newhouse.fang.com">重庆</a>
						<a target="_self" href="https://tj.newhouse.fang.com">天津</a>
						<a target="_self" href="https://wuhan.newhouse.fang.com">武汉</a>
						<a target="_self" href="https://hz.newhouse.fang.com">杭州</a>
						<a target="_self" href="https://nanjing.newhouse.fang.com">南京</a>
						<a target="_self" href="https://suzhou.newhouse.fang.com">苏州</a>
						<a target="_self" href="https://jn.newhouse.fang.com">济南</a>
						<a target="_self" href="https://sjz.newhouse.fang.com">石家庄</a>
						<a target="_self" href="https://xian.newhouse.fang.com">西安</a>
						<a target="_self" href="https://km.newhouse.fang.com">昆明</a>
						<a target="_self" href="https://wuxi.newhouse.fang.com">无锡</a>
						<a target="_self" href="https://zh.newhouse.fang.com">珠海</a>
						<a target="_self" href="https://nn.newhouse.fang.com">南宁</a>
						<a target="_self" href="https://cs.newhouse.fang.com">长沙</a>
						<a target="_self" href="https://zz.newhouse.fang.com">郑州</a>
						<a target="_self" href="https://dg.newhouse.fang.com">东莞</a>
						<a target="_self" href="https://hf.newhouse.fang.com">合肥</a>
						<a target="_self" href="https://gy.newhouse.fang.com">贵阳</a>
						<a target="_self" href="https://nb.newhouse.fang.com">宁波</a>
						<a target="_self" href="https://nc.newhouse.fang.com">南昌</a>
						<a target="_self" href="https://www.fang.com/SoufunFamily.htm">更多城市</a>





				<!--tab1_content_end-->
                </div>

				<div class="city20141104nr" id="cityi011" style="display: none;">
                <!--tab2_content_start-->

                    	<a target="_self" href="https://newhouse.fang.com">北京</a>
                    	<a target="_self" href="https://bt.newhouse.fang.com">包头</a>
                    	<a target="_self" href="https://bd.newhouse.fang.com">保定</a>

                    	<a target="_self" href="https://bh.newhouse.fang.com">北海</a>

                	    <a target="_self" href="https://changde.newhouse.fang.com">常德</a>
                		<a target="_self" href="https://cz.newhouse.fang.com">常州</a>

                    	<a target="_self" href="https://cd.newhouse.fang.com">成都</a>
                    	<a target="_self" href="https://chuzhou.newhouse.fang.com">滁州</a>
                    	<a target="_self" href="https://changchun.newhouse.fang.com">长春</a>

                    	<a target="_self" href="https://cs.newhouse.fang.com">长沙</a>

                    	<a target="_self" href="https://cq.newhouse.fang.com">重庆</a>


                    	<a target="_self" href="https://dl.newhouse.fang.com">大连</a>

                    	<a target="_self" href="https://dg.newhouse.fang.com">东莞</a>
                    	<a target="_self" href="https://fangchenggang.newhouse.fang.com">防城港</a>

                    	<a target="_self" href="https://fs.newhouse.fang.com">佛山</a>

                    	<a target="_self" href="https://fz.newhouse.fang.com">福州</a>
                    	<a target="_self" href="https://ganzhou.newhouse.fang.com">赣州</a>

                    	<a target="_self" href="https://gz.newhouse.fang.com">广州</a>

                    	<a target="_self" href="https://gy.newhouse.fang.com">贵阳</a>
                    	<a target="_self" href="https://guilin.newhouse.fang.com">桂林</a>

                    	<a target="_self" href="https://hrb.newhouse.fang.com">哈尔滨</a>
                    	<a target="_self" href="https://hn.newhouse.fang.com">海南</a>
                    	<a target="_self" href="https://hz.newhouse.fang.com">杭州</a>

                    	<a target="_self" href="https://hf.newhouse.fang.com">合肥</a>
                    	<a target="_self" href="https://hs.newhouse.fang.com">衡水</a>

                    	<a target="_self" href="https://nm.newhouse.fang.com">呼和浩特</a>


                    	<a target="_self" href="https://huangshi.newhouse.fang.com">黄石</a>

                    	<a target="_self" href="https://huizhou.newhouse.fang.com">惠州</a>
                	    <a target="_self" href="https://www.fang.com/SoufunFamily.htm">更多城市</a>


				<!--tab2_content_end-->
                </div>

                <div class="city20141104nr" id="cityi012" style="display: none;">
                <!--tab3_content_start-->

                    	<a target="_self" href="https://jl.newhouse.fang.com">吉林</a>
                    	<a target="_self" href="https://jn.newhouse.fang.com">济南</a>
                    	<a target="_self" href="https://jining.newhouse.fang.com">济宁</a>
                    	<a target="_self" href="https://jx.newhouse.fang.com">嘉兴</a>

                    	<a target="_self" href="https://jm.newhouse.fang.com">江门</a>
                    	<a target="_self" href="https://jh.newhouse.fang.com">金华</a>
                    	<a target="_self" href="https://jiujiang.newhouse.fang.com">九江</a>

                    	<a target="_self" href="https://km.newhouse.fang.com">昆明</a>
                    	<a target="_self" href="https://ks.newhouse.fang.com">昆山</a>

                    	<a target="_self" href="https://lz.newhouse.fang.com">兰州</a>

                    	<a target="_self" href="https://lf.newhouse.fang.com">廊坊</a>

                    	<a target="_self" href="https://leshan.newhouse.fang.com">乐山</a>
                    	<a target="_self" href="https://lyg.newhouse.fang.com">连云港</a>
                    	<a target="_self" href="https://linyi.newhouse.fang.com">临沂</a>
                    	<a target="_self" href="https://liuzhou.newhouse.fang.com">柳州</a>
                    	<a target="_self" href="https://luzhou.newhouse.fang.com">泸州</a>


                    	<a target="_self" href="https://ly.newhouse.fang.com">洛阳</a>
                    	<a target="_self" href="https://meizhou.newhouse.fang.com">梅州</a>
                    	<a target="_self" href="https://mianyang.newhouse.fang.com">绵阳</a>


                    	<a target="_self" href="https://nc.newhouse.fang.com">南昌</a>
                    	<a target="_self" href="https://nanchong.newhouse.fang.com">南充</a>
                    	<a target="_self" href="https://nanjing.newhouse.fang.com">南京</a>
                    	<a target="_self" href="https://nn.newhouse.fang.com">南宁</a>
                    	<a target="_self" href="https://nt.newhouse.fang.com">南通</a>

                    	<a target="_self" href="https://nb.newhouse.fang.com">宁波</a>



                    	<a target="_self" href="https://qhd.newhouse.fang.com">秦皇岛</a>

                    	<a target="_self" href="https://qd.newhouse.fang.com">青岛</a>
                    	<a target="_self" href="https://qingyuan.newhouse.fang.com">清远</a>
                    	<a target="_self" href="https://qingyang.newhouse.fang.com">庆阳</a>
                    	<a target="_self" href="https://qz.newhouse.fang.com">泉州</a>

                    	<a target="_self" href="https://sanya.newhouse.fang.com">三亚</a>
                    	<a target="_self" href="https://st.newhouse.fang.com">汕头</a>

                    	<a target="_self" href="https://sh.newhouse.fang.com">上海</a>
                    	<a target="_self" href="https://sx.newhouse.fang.com">绍兴</a>
                    	<a target="_self" href="https://sz.newhouse.fang.com">深圳</a>
                    	<a target="_self" href="https://sy.newhouse.fang.com">沈阳</a>

                    	<a target="_self" href="https://sjz.newhouse.fang.com">石家庄</a>



                    	<a target="_self" href="https://suzhou.newhouse.fang.com">苏州</a>
                    	<a target="_self" href="https://tz.newhouse.fang.com">台州</a>
                    	<a target="_self" href="https://taizhou.newhouse.fang.com">泰州</a>


                    	<a target="_self" href="https://taiyuan.newhouse.fang.com">太原</a>

                    	<a target="_self" href="https://ts.newhouse.fang.com">唐山</a>
                    	<a target="_self" href="https://tj.newhouse.fang.com">天津</a>
                		<a target="_self" href="https://www.fang.com/SoufunFamily.htm">更多城市</a>


                <!--tab3_content_end-->
                </div>

                <div class="city20141104nr" id="cityi013" style="display: none;">
                <!--tab4_content_start-->

                    	<a target="_self" href="https://weihai.newhouse.fang.com">威海</a>
                    	<a target="_self" href="https://wf.newhouse.fang.com">潍坊</a>
                    	<a target="_self" href="https://wz.newhouse.fang.com">温州</a>
                    	<a target="_self" href="https://xj.newhouse.fang.com">乌鲁木齐</a>
                    	<a target="_self" href="https://wuxi.newhouse.fang.com">无锡</a>
                    	<a target="_self" href="https://wuhu.newhouse.fang.com">芜湖</a>


                    	<a target="_self" href="https://wuhan.newhouse.fang.com">武汉</a>




                    	<a target="_self" href="https://xian.newhouse.fang.com">西安</a>
                    	<a target="_self" href="https://xn.newhouse.fang.com">西宁</a>

                    	<a target="_self" href="https://xm.newhouse.fang.com">厦门</a>
                    	<a target="_self" href="https://xz.newhouse.fang.com">徐州</a>


                    	<a target="_self" href="https://yt.newhouse.fang.com">烟台</a>
                    	<a target="_self" href="https://yancheng.newhouse.fang.com">盐城</a>

                    	<a target="_self" href="https://yz.newhouse.fang.com">扬州</a>
                    	<a target="_self" href="https://yc.newhouse.fang.com">宜昌</a>

                    	<a target="_self" href="https://yinchuan.newhouse.fang.com">银川</a>
                    	<a target="_self" href="https://yueyang.newhouse.fang.com">岳阳</a>
                    	<a target="_self" href="https://hbzy.newhouse.fang.com">枣阳</a>
                    	<a target="_self" href="https://zj.newhouse.fang.com">湛江</a>

                    	<a target="_self" href="https://zhangzhou.newhouse.fang.com">漳州</a>
                    	<a target="_self" href="https://zhenjiang.newhouse.fang.com">镇江</a>
                    	<a target="_self" href="https://zz.newhouse.fang.com">郑州</a>

                    	<a target="_self" href="https://zs.newhouse.fang.com">中山</a>
                    	<a target="_self" href="https://zhoushan.newhouse.fang.com">舟山</a>

                    	<a target="_self" href="https://zh.newhouse.fang.com">珠海</a>
                    	<a target="_self" href="https://zb.newhouse.fang.com">淄博</a>
                		<a target="_self" href="https://www.fang.com/SoufunFamily.htm">更多城市</a>

                <!--tab4_content_end-->
                </div>


					<!--more_tab_content-->
                <!--city_list_end-->
				</div>
				
			</div>
		
			<div class="s5" track-id="www1" style="background-image:none" id="dsy_H01_02">
				<div class="s4Box">
					<a href="https://wuhan.fang.com/" target="_self">首页</a>
				</div>
			</div>
		
		
			
				<div class="s5" track-id="newhouse" id="dsy_H01_03" style="">
					<div class="s4Box">
						<a href="https://wuhan.newhouse.fang.com/" target="_self">新房</a>
					</div>
					
						<div class="listBox">
							<ul>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/house/saledate/%b1%be%d4%c2.htm">
															本月开盘
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/house/asp/trans/buynewhouse/default.htm">
															热门楼盘
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/house/livindate/%b1%be%d4%c2.htm">
															本月交房
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/newblog/">
															楼盘新动态
                                                    </a>
												
									</li>
								
									<li style="">
										        
                                                    
                                                    <a  id="dsy_D01_104"  target="_self" style="color:red" href="https://m.fang.com/club/?channel=newhouse&city=wuhan">
                                                        
                                                            <div>特价房</div>
                                                        
                                                    </a>
                                                    
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/house/daogou/index.htm">
															楼盘导购
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/top/">
															新房排行榜
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="color:#f00;" href="https://wuhan.newhouse.fang.com/house/s/d21/">
															知名学校
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://zhishi.fang.com/xf/">
															购房知识
                                                    </a>
												
									</li>
								
									<li style="">
										        
													<a  target="_self" style="" href="https://wuhan.newhouse.fang.com/house/kanfangtuan.htm">
															看房团
                                                    </a>
												
									</li>
								
									<li style="margin-bottom:8px">
										        
                                                    
                                                    <a  id="dsy_D01_81"  target="_self" style="" href="https://m.fang.com/club/?channel=newhouse&city=wuhan">
                                                        
                                                            <div class="butstyle20141104">特价房</div>
                                                        
                                                    </a>
                                                    
												
									</li>
								
                            </ul>
                        </div>
                    
                </div>
            

					
						<div class="s6" track-id="esf" id="dsy_H01_04" style="" >
							<div class="s4Box">
								<a href="https://wuhan.esf.fang.com/" target="_self">二手房</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/"   style="" >
													
														在售房源
													
												</a>
												
											</li>
										
											
												
													<li>
														<a target="_self" href="https://wuhan.esf.fang.com/house/a21/?push_from=fang_indexbanneresf_pc">
															业主真房源
														</a>
													</li>
												
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/house/t11/"   style="" >
													
														特价房
													
												</a>
												
											</li>
										
											
											<li style=""  class="hp_add">
												<a target="_self" href="https://wuhan.esf.fang.com/housing/"   style="" >
													
														找小区
													
												</a>
												
													<i></i>
												
											</li>
										
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/school/"   style="" >
													
														找学校
													
												</a>
												
											</li>
										
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/agenthome/"   style="" >
													
														找经纪人
													
												</a>
												
											</li>
										
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/house/z63/"   style="" >
													
														找别墅
													
												</a>
												
											</li>
										
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/top/"   style="" >
													
														二手房排行榜
													
												</a>
												
											</li>
										
											
											<li style=""  class="">
												<a target="_self" href="https://zhishi.fang.com/esf/"   style="" >
													
														购房知识
													
												</a>
												
											</li>
										
											
											<li style=""  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/my/usercenter/housepublish/ebhousepublish/"   style="" >
													
														我要卖房
													
												</a>
												
											</li>
										
											
											<li style="margin-bottom:8px"  class="">
												<a target="_self" href="https://wuhan.esf.fang.com/live/search/"  id="dsy_D01_200"   style="" >
													
														<div class="butstyle20141104">直播看房</div>
													
												</a>
												
											</li>
										
									</ul>
								</div>
							
						</div>
					
					
						<div class="s5" track-id="zu" id="dsy_H01_05" >
							<div class="s4Box">
								<a href="https://wuhan.zu.fang.com/" target="_self">租房</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											<li style="" >
												<a target="_self" href="https://wuhan.zu.fang.com/"  id="dsy_D01_116" >
													
														在租房源
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self" href="https://wuhan.zu.fang.com/house/a21/" >
													
														个人房源
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self" href="https://wuhan.zu.fang.com/house/n31/" >
													
														整租房源
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self" href="https://wuhan.zu.fang.com/hezu/" >
													
														合租房源
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self" href="https://wuhan.zu.fang.com/villa/" >
													
														别墅房源
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self" href="https://zhishi.fang.com/zf/" >
													
														租房知识
													
												</a>
											</li>
										
											<li style="margin-bottom:8px" >
												<a target="_self" href="https://wuhan.zu.fang.com/chuzuinput/" >
													
														<div class="butstyle20141104">免费发布出租</div>
													
												</a>
											</li>
										
									</ul>
								</div>
							
						</div>
					
					
						<div class="s6" track-id="fangjia" style="background-image:none" id="dsy_H01_06">
							<div class="s4Box">
								<a href="https://fangjia.fang.com/wuhan/" target="_self">查房价</a>
							</div>
						</div>
					

					
						<div class="s7" track-id="home" id="dsy_H01_07" >
							<div class="s4Box">
								<a href="https://wuhan.home.fang.com/" target="_self">装修家居</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											<li style="" >
												<a target="_self"   style=""  href="//wuhan.home.fang.com/zhuangxiu/">
													
														家装案例
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style="color:#f00;"  href="https://home.fang.com/dianpu/wuhan/">
													
														直播旺铺
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://home.fang.com/riji/">
													
														装修日记
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://home.fang.com/album/wuhan/">
													
														装修效果图
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"  id="dsy_D01_39"   style=""  href="https://zhishi.fang.com/jiaju/">
													
														装修攻略
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://wuhan.home.fang.com/news/">
													
														家居资讯
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://wuhan.home.fang.com/jiancai/">
													
														建材家具
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://wuhan.home.fang.com/jiancai/shop/">
													
														建材店铺
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://home.fang.com/newdesign.htm?postion=daohang">
													
														免费设计
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"   style=""  href="https://home.fang.com/newyanfang.htm?postion=daohang">
													
														免费验房
													
												</a>
											</li>
										
											<li style="margin-bottom:8px" >
												<a target="_self"   style=""  href="https://home.fang.com/zxbj/?from=daohang">
													
														<div class="butstyle20141104">装修报价</div>
													
												</a>
											</li>
										
									</ul>
								</div>
							
						</div>
					
					
						<div class="s6" track-id="office" id="dsy_H01_08" >
							<div class="s4Box">
								<a href="https://wuhan.office.fang.com/" target="_self">写字楼</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											<li style="" >
												<a target="_self"  href="https://wuhan.office.fang.com/zu/house/">
													
														写字楼出租
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"  href="https://wuhan.office.fang.com/shou/house/">
													
														写字楼出售
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"  href="https://wuhan.newhouse.fang.com/house/s/a75/">
													
														写字楼新盘
													
												</a>
											</li>
										
									</ul>
								</div>
							
						</div>
					
					
						<div class="s5" track-id="shop" id="dsy_H01_09" >
							<div class="s4Box">
								<a href="https://wuhan.shop.fang.com/" target="_self">商铺</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											<li style="" >
												<a target="_self"  id="dsy_D01_46"  href="https://wuhan.shop.fang.com/zu/house/">
													
														商铺出租
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"  href="https://wuhan.shop.fang.com/shou/house/">
													
														商铺出售
													
												</a>
											</li>
										
											<li style="" >
												<a target="_self"  id="dsy_D01_48"  href="https://wuhan.newhouse.fang.com/house/s/a72/">
													
														商铺新盘
													
												</a>
											</li>
										
									</ul>
								</div>
							
						</div>
					
					<div class="s7" track-id="bbs" id="dsy_H01_04" style="background-image:none">
						<div class="s4Box">
							<a href="https://world.fang.com" target="_self">海外房产</a>
						</div>
						<div class="listBox">
							<ul>
								<li><a href="https://world.fang.com/house/ctus/" target="_self">美国房产</a></li>
								<li><a href="https://world.fang.com/house/ctau/" target="_self">澳大利亚房产</a></li>
								<li><a href="https://japan.fang.com/" target="_self">日本房产</a></li>
								<li><a href="https://world.fang.com/house/ctuae/" target="_self">阿联酋房产</a></li>
								<li><a href="https://uk.fang.com" target="_self">英国房产</a></li>
								<li><a href="https://malaysia.fang.com" target="_self">马来西亚房产</a></li>
								<li><a href="https://singapore.fang.com/" target="_self">新加坡房产</a></li>
							</ul>
						</div>
					</div>
					
						<div class="s7" track-id="news" id="dsy_H01_14" >
							<div class="s4Box">
								<a href="https://wuhan.news.fang.com/" target="_self">房产百科</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											<li style="">
												<a target="_self"  href="https://wuhan.news.fang.com/gdxw.html">
													
														房产快讯
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://wuhan.news.fang.com/more/201312398/1.html">
													
														房产圈
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://wuhan.news.fang.com/more/32/1.html">
													
														市场
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://wuhan.news.fang.com/more/35/1.html">
													
														政策
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://www.fang.com/ask/wuhan/">
													
														房产问答
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://zhishi.fang.com/">
													
														房产知识
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://wuhan.news.fang.com/more/736/1.html">
													
														金融
													
												</a>
											</li>
										
											<li style="">
												<a target="_self"  href="https://wuhan.news.fang.com/more/737/1.html">
													
														土地
													
												</a>
											</li>
										
										<li>
											<a target="_self" id="dsy_D01_132" href="https://baike.fang.com/">百科</a>
										</li>
									</ul>
								</div>
							
						</div>
					

					

					
						<div class="s5" style="background-image:none">
							<div class="s4Box">
								<a id="dsy_H01_26" href="https://live.fang.com/liveshow/index/list_wuhan_1" target="_self">直播看房</a>
							</div>
						</div>
					

					
						<div class="s5" track-id="more" id="dsy_H01_21" style="" >
							<div class="s4Box">
								<a id="dsy_D01_91">更多</a>
							</div>
							
								<div class="listBox">
									<ul>
										
											<li class="new">
												<div class="s8" onmouseover="this.className='s8 on'" onmouseout="this.className='s8'">
													
														<a href="http://fdc.fang.com/"   target="_self">产业</a>
													
													
														<div class="listnBox top2">
															<ul>
																
																	
																		
																			<li>
																				<a href="http://land.fang.com/">土地</a>
																			</li>
																		
																	
																		
																			<li>
																				<a href="http://fdc.fang.com/data/">地产数据</a>
																			</li>
																		
																	
																		
																			<li>
																				<a href="http://fdc.fang.com/wenku/">文库报告</a>
																			</li>
																		
																	
																		
																	
																		
																			<li>
																				<a href="http://fdc.fang.com/top10/">房企研究</a>
																			</li>
																		
																	
																		
																	
																		
																			<li>
																				<a href="http://fdc.fang.com/index/BaiChengIndex.html">百城价格指数</a>
																			</li>
																		
																	
																		
																			<li>
																				<a href="https://creis.fang.com/">中指数据库</a>
																			</li>
																		
																	
																
															</ul>
														</div>
													
												</div>
											</li>
										
											<li class="new">
												<div class="s8" onmouseover="this.className='s8 on'" onmouseout="this.className='s8'">
													
														<a href="https://wuhan.bbs.fang.com/" id="dsy_D01_12" target="_self">业主论坛</a>
													
													
														
															<div class="listnBox top3">
																<ul>
																	
																		<li style="" >
																			<a target="_self"  href="https://wuhan.bbs.fang.com/index.php?_c=Managerindex&amp;_m=EliteList">
																				
																					精华帖
																				
																			</a>
																		</li>
																	
																		<li style="" >
																			<a target="_self"  href="https://wuhan.bbs.fang.com/asp/index/busiActivityMore.aspx">
																				
																					业主活动
																				
																			</a>
																		</li>
																	
																		<li style="" >
																			<a target="_self"  href="https://wuhan.home.fang.com/bbs/">
																				
																					装修论坛
																				
																			</a>
																		</li>
																	
																		<li style="" >
																			<a target="_self"  id="dsy_D01_68"  href="https://wuhan.bbs.fang.com/board/whmf/">
																				
																					购房圈
																				
																			</a>
																		</li>
																	
																</ul>
															</div>
														
													
												</div>
											</li>
										
											<li class="new">
												<div class="s8" onmouseover="this.className='s8 on'" onmouseout="this.className='s8'">
													
														<a href="https://wuhan.newhouse.fang.com/fangpaiquan/"   target="_self">VR全景看房</a>
													
													
												</div>
											</li>
										
										
									</ul>
								</div>
							
						</div>
					
				
				

<div id="loginBarNew">
<div class="s4a" onmouseover="this.className='s4a on2014' " style="width:70px;" onmouseout="this.className='s4a';" >
                <div class="s4Box"><a id="dsy_H01_25" href="javascript:void(0);" >更多服务</a></div>
                <div class="listBox" id="dsy_D01_89" style="width:68px;">
                	<ul>
			            <li style="text-align:center;padding-left:0"><a href="https://3.fang.com/" target="_blank" id="dsy_D01_6717">家居云</a></li>
			            <li style="text-align:center;padding-left:0"><a href="http://2.3fang.com/" target="_blank" id="dsy_D01_6772">商办云</a></li>
						
							<li style="text-align:center;padding-left:0"><a href="https://1.fang.com/" target="_blank" id="dsy_H01_24">开发云</a></li>
						
					</ul>

                </div>
            </div>

	

	<div id="dsy_H01_23" class="s4a" onmouseover="this.className='s4a on2014' " style="background-image:none;" onmouseout="this.className='s4a';">
        <div class="s4Box"><a href="https://2.fang.com/" target="_blank">经纪云</a></div>
        <div class="listBox" style="display:none;"></div>
	</div>
	<div class="sline21041104" id="slineId"></div>
	<div id="dsy_H01_22"  class="s4a" onmouseover="this.className='s4a on2014';hideQipao()" onmouseout="this.className='s4a';qipao();" style="width:80px">
    	<div class="s4Box" style="text-overflow: ellipsis">
    	<div class="guidance" style="display:none;"></div>
    		<a href="javascript:void(0);" onmouseover="changeLoginUrl();" onclick="changeLoginUrl();" id="sfHeadUsername" onmouseout="qipao();">
            登录
    		</a>
    		<input type="hidden" id="userCenterUrl" value="https://my.fang.com/" />
    	</div>
		<div class="listBox" id="">
        	<ul>
        		<li id="signUpli"><a id="signUp" href="javascript:void(0);" onmouseover="changeSignUrl();" onclick="changeSignUrl();" target="_blank">立即注册</a></li>
               	<li><a href="https://my.fang.com/" target="_blank">我的房天下</a></li>

                   
               		 
               					<li><a href="https://qd.newhouse.fang.com/club/?city=wuhan" target="_blank">直播看房</a></li>
               				
               		

               	<li><a href="https://mp.fang.com" target="_blank">入驻房产圈</a></li>
            </ul>
            <div id=""  class="tuic" style="display: none;"><a href="http://dianpu.fang.com/" id="sfHeadRegister">退出</a></div>
        </div>
	</div>
</div>
<div class="clear"></div>
				<input type="hidden" id="serviceline" value="newhouse"/>
			</div>
		</div>

		<script type="text/javascript" src="//static.soufunimg.com/navigation/newnav20141111.js?v="></script>
		<!-- login js start -->
		<script type="text/javascript" src="//static.soufunimg.com/homepage/new/family/js/loginUnited.js?v=" charset="GBK"></script>
		<!-- login js end -->
		<!-- 导航 end  -->



    
    
        
        <!--搜索文件开始-->
<link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/common/search_public.css?v=202109160001" rel="stylesheet"/>
<div class="main_1200 searchBox" id="" style="position:relative;z-index:1201;">
	<div class="box clearfix">
		<div class="s_box" style="padding-top:15px;" >
			<!-- search begin -->
			<div class="clearfix pr" style="padding-bottom:10px; z-index:99;" >
				<div id="xf_C01_01"  style="float:left">
				<div class="box_input fl" id="search_container"  style="position:relative;z-index:9998">
					<div id="search_form" class="search_div">
						<input type="text" class="search" placeholder="请输入关键字(楼盘名/地名/开发商等)" id="search_box"  autocomplete="off" style="color: rgb(102, 102, 102);" />
					</div>
					<input type="button" value="搜&nbsp;索" class="sear_btn" id='searchBtn'>
					<img id="advImg" src="//imgd.soufunimg.com/2016/07/19/25k/5c7d1e9a085b40e783e5818af3af8b20.png" alt="" style="position:absolute;top:12px;right:92px;">
				</div>
				</div>
				<div class="hot clearfix tf fl" style="float:left" id="xfptxq_B02_05">
					<ul>
						
						<li><a  target="_blank"  href="//wuhan.newhouse.fang.com/house/daogou/index.htm" style="color:red;">楼盘导购</a></li>
						
						
							
							<li><a href="https://wuhan.newhouse.fang.com/house/saledate/201908.htm" target="_blank">本月开盘</a></li>
							
							<li><a href="http://wuhan.newhouse.fang.com/house/saledate/%b1%be%d4%c2.htm?fptn=pc_wuhan_sfsy_ssbq" target="_blank">本月开盘</a></li>
							
							<li><a href="http://wuhan.newhouse.fang.com/house/s/list/b28000%2C10000/?fptn=pc_wuhan_sfsy_ssbq" target="_blank">8千-1万</a></li>
							
							<li><a href="http://wuhan.newhouse.fang.com/house/s/list/b25000%2C8000/?fptn=pc_wuhan_sfsy_ssbq" target="_blank">5千-8千</a></li>
							
							<li><a href="http://wuhan.newhouse.fang.com/house/s/b4138-b7rail/" target="_blank">6号线</a></li>
							
						
					</ul>
				</div>
			</div>
			<!-- search end -->
		</div>
	</div>
</div>
<!--搜索文件结束-->







        
     
    
    
<link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/common/fixnav.css?v=202109160001" rel="stylesheet"/>
<script type="text/javascript">
function loadScript(B,D){var A=document.createElement("script"),C=document.documentElement.firstChild;A.type="text/javascript";if(A.readyState){A.onreadystatechange=function(){if(A.readyState=="loaded"||A.readyState=="complete"){A.onreadystatechange=null;D()}}}else{A.onload=function(){D()}}A.src=B;C.insertBefore(A,C.firstChild)};
</script>
<!--新搜索 begin-->
<div id="floatNaviBox" class="fixnav" style="display:none;">
    <div class="main_1200 pr">
        <div class="fixnav_tit" id="xfptxq_B02_01">
			<h2 class="tf"><a href="//wuhan.newhouse.fang.com/loupan/2610156494.htm">华侨城·欢乐天际</a></h2>
			<span id="phone400_fixnavs">
			
				
                    
                    <span class="ml15" style="font-size: 18px;font-weight: bold;">4001891932</span>  
                    				
				
			</span>
		</div>
        <div class="tbsearch" id="xfptxq_B02_02">
			<div target="_blank" >
				<input type="hidden" id="strDistrict_2" name="strDistrict" />
				<input type="hidden" id="strComarea_2" name="strComarea" />
				<input type="hidden" id="strNamekeyword_2" name="strNamekeyword" />
				<input type='text' style='display:none'> 
				<div class="fl pr" > 
					<input suggestion="y" suggestiontype="lp" autocomplete="OFF" placeholder="请输入关键字(楼盘名/地名/开发商等)" name="searchinput_2" id="searchinput_2" type="text" class="tbsearchinput f14 tf">
					<div id="suggest-div"  class="suggest-div" style="width:322px;position:absolute;top:32px; left:0px;">
						<table  id="suggesttable_2" width="100%" border="0" cellpadding="0" cellspacing="0" style="display:none" class="tyka tf">
							<tbody>
								<tr style="display:none;">
									<td></td>
								</tr>
							</tbody>
						</table>	
					</div>
				</div>
				<div class="fl"> 
					<input class="tf tbsearchbtns" type="button" name="" id="fixnavSearchBtn" value="搜&nbsp;索"> 
					<img id="advImg2" src="//imgd.soufunimg.com/2016/07/19/25k/5c7d1e9a085b40e783e5818af3af8b20.png" alt="" style="position:absolute;top:18px;right:109px;">
				</div> 
			</div>
        </div>
		 <!-- 手机下载app beigin --> 
            <div class="fang_logo tf" id="xfptxq_B02_03"> 
                <img src="//img1.soufunimg.com/house/images/fang_logo.jpg" width="30" height="30" class="vm" onmousemove="oversh('show');" onmouseout="oversh('hide');" > 
                <div class="phone_bt_tc_fix" style="display:none;" id="ewm" > 
                    <img src="//img1.soufunimg.com/house/images/qrcode_housedetail.png" width="90" height="90" class="vm"> 
                    <p>扫描下载<br>房天下APP</p> 
                </div> 
            </div> 
          <!-- 手机下载app end -->
    </div>
</div>

<div class="main_1200 tf">
	<!-- 面包屑 begin -->
	<div class="breadcrumb">
    
    <div class="br_left">
        <div>
            <ul class="tf f12" id="xfptxq_B02_06">
                <li><a target="_blank" href="//www.fang.com/">房天下</a>&nbsp;&gt;&nbsp;</li>
                
                    
                        <li><a target="_blank"  href="//wuhan.newhouse.fang.com/house/s/">武汉新房</a>&nbsp;&gt;&nbsp;</li>
                        <li><a target="_blank" href="//wuhan.newhouse.fang.com/house/s/hongshan/" title="洪山新楼盘">洪山楼盘</a>&nbsp;&gt;&nbsp;</li>
                    
                
                
                    <li><a target="_blank" href="//wuhan.newhouse.fang.com/loupan/2610156494.htm" title="华侨城·欢乐天际">华侨城·欢乐天际</a>&nbsp;&gt;&nbsp;</li>
                    <li>华侨城·欢乐天际楼盘详情</li>
                
            </ul>
        </div>
    </div>  
</div>

	<!-- 面包屑 end -->
	<!-- 二级导航 begin -->
	<div class="lpname">
	<dl style="width:50%;">
		<dt><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAklEQVR4AewaftIAAASbSURBVOXBQW7jCBDAQNLQ/7/MTR8aEATLdmZzc5X94Is9+HIPvtyDL/fgyz34cgc3VD5RMVRGxVJZFUulYqisCpWKpXKnYqh8ouLqwZc7eKPijsqqUFkqFVcqFatiqVSojIpVoTIqriruqNw5+IDKWcUzFavijsqqUFkqFUOl4jdUzipeOfgjKq9UrIo7FSpXKktlVPxfD77cwR+qUFkVz6hUDJWKpfJMhcpfO/hAxSdUKoaKyqh4RWVUnFU8U3Gn4jcefLmDN1Q+VaEyKlSWyqhQOasYKhUqS2VUnKlULJV/cXCj4rdUKobKWcWZylIZFXdUzipWxb968OUObqiMijOViqFyVqFypXJWsVTuqKwKlaFSofJKxVAZFVcHNyqGSoXKUhkVS+WsYqmsCpWKUaEyVEbFUHmmYlRcqVQMlVFx5+ADKhVLZajcUakYFXdUKobKHZWlMiqGSsUzFa88+HL2gzdUziqWyqgYKqNiqVScqYyKM5WKpTIqVEaFSsUzKmcVd+wHT6iMCpVVofJMxR2VVaEyKlTuVLyjsirOVFbF1YMvZz94QeWsQmVUqIwKlVWh8omKM5V3Kp5RWRXvHNxQGRVDZahUDJWKVbFUXqkYKkvlqmKp3FG5UhkVdx58uYM3VCoqlsqoUBkVKhWjQuWZilVxVTFUVEbFqhgqz1QMlXcOblQMlTOViqFyVqGyKobKqlCpWCqrYlXcUakYKqtCZVWojIor+8EHVK4qVEaFSsVQWRVXKlcVQ+Wq4kxlVSyVVaFScefBl7MfPKHyiYqhMiqWyqoYKhVLZVUMlVWxVEbFmUrFlUrFKwdvVAyVUXGmcqbyjsqqUBkqn1K5o7JUKu48+HL2gxdUKs5UVsVQeaXiTGVULJU7FSqjYqhcVfzGwRsVQ2VUrAqVUTFURsVSWSqjYqhUjAqViqFScaUyKpbKUKlYKqvi6uCGyqhQqRgqFUPlX1SojIqzijsVQ+UVlbOKOw++3MGNimcqVEaFyjMqq0JlVJyprIqhMipUVsWoGCrPVAyVilfsB2+onFUMlbOKM5VnKpbKqhgqn6hYKncq7jz4cvaDJ1SeqbijUjFUziqWSsVSWRVLpeKOyqoYKhWfsh/8gkrFUKk4UxkVZyqjQuWsYqiMiqVyVfFXHny5gw+orAqVUbFUKs5UnqlQuapQWSoVS+VM5ariSmVUXB3cUFkVKkOlYqisilcqhkrFqlAZFUNlqYyKiqXyjErFUKmouGM/+AMqVxVL5ZmKOyqr4kyl4kqlYqlU3Hnw5Q5uqHyiYlUsFZVVMVQqlkrFULmqGCqr4kyl4l8cvFFxR2VVDJVRoXJVoVIxKlaFSsVSWRXPVJyprIpXHny5gw+onFVcqVRUDJWK31CpeKZCZVQMlXdUVsXVwR+pGCqj4k7FUlkVQ2VUVKyKoVKhclWxVCpeefDlDv6QSsWVylnFHZWKpTIqzlTOKpbKUqm4c/CBit9SqRgVKkvlGZWh8omKK5VVofLKwRsqn1CpWBVLpeJMZVQslbMKlWcqVEaFyqhQOVMZFVcPvpz94Is9+HIPvtyDL/fgy/0Hw3C6nCllZ8YAAAAASUVORK5CYII=" width="64" height="64"></dt>
		<dd>
			<div class="lpbt">
				<h1 style="font-size:26px !important;"><a class="ts_linear" id="huxinxq_E02_15" href="//wuhan.newhouse.fang.com/loupan/2610156494.htm" title="华侨城·欢乐天际" target="_blank">华侨城·欢乐天际</a></h1>
				
			</div>
			<div class="lpicon">
			
			<a class="bgred" href="//wuhan.newhouse.fang.com/house/s/c44/" target="_blank" >在售</a>
			
			<a class="bgblue" href="//wuhan.newhouse.fang.com/house/s/a77/" target="_blank" >普通住宅</a>
			
			<a class="bgblue" href="//wuhan.newhouse.fang.com/house/s/a77/" target="_blank" >商住公寓</a>
			
			<a class="bgblue" href="//wuhan.newhouse.fang.com/house/s/a77/" target="_blank" >LOFT</a>
			
			<a class="bgblue" href="//wuhan.newhouse.fang.com/house/s/b33/" target="_blank" >品牌地产</a>
			
			</div>
		</dd>
	</dl>
</div>
<style>
 .searchBox {background:#f7f7f7;width:100%}
</style>
<div class="cxfnav" id="orginalNaviBox">
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494.htm" id="xfptxq_B03_06">楼盘首页</a>
		
	
		
		<a class="cur" href="https://wuhan.newhouse.fang.com/loupan/2610156494/housedetail.htm" id="xfptxq_B03_08">楼盘详情</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/dongtai/" id="xfptxq_B03_012">楼盘动态</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/photo/" id="xfptxq_B03_016">楼盘相册</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/photo/list_900.htm" id="xfptxq_B03_010">户型</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/housereport.html" id="xfptxq_B03_010">楼盘报告</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/dianping/" id="xfptxq_B03_017">点评</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/fangjia.htm" id="xfptxq_B03_011">房价走势</a>
		
	
		
		<a class="" href="https://wuhan.newhouse.fang.com/loupan/2610156494/zhuangxiu/" id="xfptxq_B03_015">装修效果图</a>
		
	
</div>

	<!-- 二级导航 end -->
	<!--主体内容 start-->
    <div class="blank8"></div>
    <div class="main_1200">
        <!--内容区开始-->
        <div class="main-cont clearfix">
            <!--左侧内容开始-->
            <div class="main-left">
                <!--基本信息开始-->
                <div class="main-item">
                    <h3>基本信息</h3>
                    <div class="main-info clearfix" style="padding-bottom:5px;">
                        <div class="main-info-price">
                            <div class="titN">价<i style="margin-right:28px"></i>格：</div>
                            <div class="pricetd">
                                
                                <p><b></b><em>21000元/平方米起</em></p>
                                
                                <p><b></b><em>14000元/平方米起</em></p>
                                
                            </div>
                        </div>
                        <div class="main-info-comment">
                            <span class="tit">用户点评：</span>
                            
                            <a href="//wuhan.newhouse.fang.com/loupan/2610156494/dianping/" class="comment">
                                <span class="star">
                                <script>
									var zongfen_halfstar = 1;
									var zongfen_allstar = 4;
									var zongfen_huistar = 0;
									for (var i = 0;i < zongfen_allstar;i++){
										document.write('<i></i>');
									};
									if(zongfen_halfstar){
										document.write('<i class="half-star"></i>');
									}
									for (var i = 0;i < zongfen_huistar;i++){
										document.write('<i class="gray-star"></i>');
									}
								</script>
                                </span>
                                <span style="margin-right: 5px;">4.95</span>
                                <span>[910条点评]</span>
                            </a>
                            
                        </div>
                    </div>
                    <ul class="list clearfix">
                        <li>
                            <div class="list-left">物业类别：</div>
                            <div class="list-right" title="普通住宅,商住公寓,LOFT">普通住宅,商住公寓,LOFT</div>
                        </li>
                        <li>
                        <div class="list-left">项目特色：</div>
                        <div class="list-right" style="height:32px;">
                            
                                
                                    <span class="tag">品牌地产</span>
                                
                                    <span class="tag">地铁沿线</span>
                                
                            
                        </li>
                        <li>
                            <div class="list-left">建筑类别：</div>
                            <div class="list-right">
                                <span class="bulid-type">板楼</span>
                            </div>
                        </li>
                        <li>
                            <div class="list-left">装修状况：</div>
                            <div class="list-right">
                                
                                    毛坯
                                
                            </div>
                        </li>
                        <li>
                            <div class="list-left">产权年限：</div>
                            <div class='list-right'>
                                <div class='clearfix cqnx_512'>
                                    
                                        
                                        <p style="width: 150px;float: left;">普通住宅:70年</p>
                                        
                                        <p style="width: 150px;float: left;">商住公寓:40年</p>
                                        
                                        <p style="width: 150px;float: left;">LOFT:40年</p>
                                        
                                    
                                </div>
                            </div>
                        </li>
                        
                        <li>
                            <div class="list-left">环线位置：</div>
                            <div class="list-right">二至三环</div>
                        </li>
                        
                        <li class="list-text">
                            <div class="list-left">开<i style="margin-right: 6px;"></i>发<i style="margin-right: 6px;"></i> 商：</div>
                            <div class="list-right-text"><a href="https://baike.fang.com/item/武汉华侨城实业发展有限公司/1216199" target="_blank">武汉华侨城实业发展有限公司</a></div>
                        </li>
                        <li class="list-text">
                            <div class="list-left">楼盘地址：</div>
                            <div class="list-right-text">团结大道地铁4号线工业四路站B出口</div>
                        </li>
                    </ul>
                </div>
                <!--基本信息结束-->
                <!--销售信息开始-->
                <div class="main-item">
                    <h3>销售信息</h3>
                    <ul class="list clearfix">
                        <li>
                            <div class="list-left">销售状态：</div>
                            <div class="list-right">在售</div>
                        </li>
                        <li>
                            <div class="list-left">开盘时间：</div>
                            <div class="list-right">2021年8月31日已推出L14、L17号楼<a href="//wuhan.newhouse.fang.com/loupan/2610156494/dongtai/4_1/" target="_blank" class="item-a">[开盘时间详情]</a></div>
                        </li>
                        <li>
                            <div class="list-left">交房时间：</div>
                            <div class="list-right">预计2023年12月交付<a href="//wuhan.newhouse.fang.com/loupan/2610156494/dongtai/5_1/" target="_blank" class="item-a">[交房时间详情]</a></div>
                        </li>
                        <li>
                            <div class="list-left">售楼地址：</div>
                            <div class="list-right" title="洪山区团结大道地铁4号线工业四路站B出口">洪山区团结大道地铁4号线工业四路站B出口</div>
                        </li>
                        <li>
                            <div class="list-left">咨询电话：</div>
                            <div class="list-right c00">4001891932</div>
                        </li>
                        <li class="list-text">
                            <div class="list-left">主力户型：</div>
                            <div class="list-right-text">
                                
                                    
                                        <a href="//wuhan.newhouse.fang.com/loupan/2610156494/photo/list_900.htm">4居(建面130㎡)</a> 
                                    
                                        <a href="//wuhan.newhouse.fang.com/loupan/2610156494/photo/list_900.htm">4居(建面130㎡)</a> 
                                    
                                        <a href="//wuhan.newhouse.fang.com/loupan/2610156494/photo/list_900.htm">4居(建面143㎡)</a> 
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                        
                                    
                                
                            </div>
                        </li>
                        <li class="list-text">
                            <div class="list-left w84">预售许可证：</div>
                            <div class="list-right-text w730"></div>
                        </li>
                    </ul>
                    
                    <div class="main-table">
                        <div class="table-part">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="224">预售许可证</td>
                                <td width="175">发证时间</td>
                                <td width="364">绑定楼栋</td>
                                <td width="150">网上销控表</td>
                            </tr>
                            
                                
                                <tr>
                                    <td>武房开预售[2021]679号</td>
                                    <td>2021-08-27</td>
                                    <td class="td-left">L14#,L17#</td>
                                    <td><a></a></td>
                                </tr>
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                        </table>
                        
                        <div class="btn-open">展开<i></i></div>
                        
                        </div>
                        
                        <div class="table-all" style="display: none;">
                        <table cellpadding="0" cellspacing="0">

                            <tr>
                                <td width="320">预售许可证</td>
                                <td width="150">发证时间</td>
                                <td width="320">绑定楼栋</td>
                                <td width="150">网上销控表</td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]679号</td>
                                <td>2021-08-27</td>
                                <td class="td-left">L14#,L17#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]609号</td>
                                <td>2021-07-30</td>
                                <td class="td-left"></td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]576号</td>
                                <td>2021-07-19</td>
                                <td class="td-left">L13#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]467号</td>
                                <td>2021-05-28</td>
                                <td class="td-left">Y15#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]188号</td>
                                <td>2021-03-26</td>
                                <td class="td-left">L11#,L8#,L9#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]187号</td>
                                <td>2021-03-26</td>
                                <td class="td-left">L12#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2021]150号</td>
                                <td>2021-03-19</td>
                                <td class="td-left">Y10#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2020]927号</td>
                                <td>2020-11-25</td>
                                <td class="td-left">L3#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2020]926号</td>
                                <td>2020-11-25</td>
                                <td class="td-left">L1#</td>
                                <td><a></a></td>
                            </tr>
                            
                            <tr>
                                <td>武房开预售[2020]795号</td>
                                <td>2020-10-29</td>
                                <td class="td-left">L4#</td>
                                <td><a></a></td>
                            </tr>
                            
                        </table>
                        <div class="btn-off">收起<i></i></div>
                        </div>
                        
                    </div>
                    
                </div>
                <!--销售信息结束-->
                
                <!--小区规划开始-->
                <div class="main-item">
                    <h3>小区规划</h3>
                    <ul class="clearfix list">
                        <li>
                        <div class="list-left">占地面积：</div>
                        <div class="list-right">260000 ㎡</div>
                        </li>
                        <li>
                        <div class="list-left">建筑面积：</div>
                        <div class="list-right">2400000 ㎡</div>
                        </li>
                        <li>
                        <div class="list-left">容<i style="margin-right: 6px;"></i>积<i style="margin-right: 6px;"></i>率：</div>
                        <div class="list-right">3.57&nbsp; </div>
                        </li>
                        <li>
                        <div class="list-left">绿<i style="margin-right: 6px;"></i>化<i style="margin-right: 6px;"></i>率：</div>
                        <div class="list-right">30%</div>
                        </li>
                        <li>
                        <div class="list-left">停<i style="margin-right: 6px;"></i>车<i style="margin-right: 6px;"></i>位：</div>
                        <div class="list-right">3170个停车位；公寓配652个，每100㎡配套1.2个车位</div>
                        </li>
                        <li>
                        <div class="list-left">楼栋总数：</div>
                        <div class="list-right">18栋</div>
                        </li>
                        
                            <li>
                                <div class="list-left">总<i style="margin-right: 6px;"></i>户<i style="margin-right: 6px;"></i>数：</div>
                                <div class="list-right">2293户</div>
                            </li>
                        
                        <li>
                        <div class="list-left">物业公司：</div>
                        <div class="list-right">深圳华侨城物业服务有限公司</div>
                        </li>
                        <li>
                        <div class="list-left">物<i style="margin-right: 6px;"></i>业<i style="margin-right: 6px;"></i>费：</div>
                        <div class="list-right">3.2元/㎡·月&nbsp;</div>
                        </li>
                        <li class="list-text">
                        <div class="list-left" style="width:90px">物业费描述：</div>
                        <div class="list-right-floor" style="width:730px">3.2~3.8元/㎡/月</div>
                        </li>
                        <li class="list-text">
                        <div class="list-left">楼层状况：</div>
                        <div class="list-right-floor">5栋6F洋房；13栋32-60F高层；公寓42层</div>
                        </li>
                    </ul>
                </div>
                <!--小区规划结束-->
                <!--价格信息开始-->
                
                <div class="main-item">
                    <h3><a href="//wuhan.newhouse.fang.com/loupan/2610156494/fangjia.htm" target="_blank" class="price-trend">查看价格走势 &gt;</a>价格信息</h3>
                    <div class="main-table">
                        <div class="table-part">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="110">记录时间</td>
                                <td width="90">均价</td>
                                <td width="90">起价</td>
                                <td width="342">价格描述</td>
                            </tr>
                            
                                
                                    <tr>
                                    <td>2021-09-17</td>
                                    <td> </td>
                                    <td>约21000元/㎡</td>
                                    <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享95折优惠，另有部分特价房源享受9折优惠～三期新品火爆热销中，欲购从速~</td>
                                    </tr>
                                
                            
                                
                                    <tr>
                                    <td>2021-09-15</td>
                                    <td> </td>
                                    <td>约21000元/㎡</td>
                                    <td class="td-left">华侨城·欢乐天际已签约武汉小学，建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享95折优惠，另有部分特价房源；优惠多多，先到先得～即将加推三期新品，敬请期待！</td>
                                    </tr>
                                
                            
                                
                                    <tr>
                                    <td>2021-08-31</td>
                                    <td> </td>
                                    <td>约21000元/㎡</td>
                                    <td class="td-left">华侨城·欢乐天际已签约武汉小学，建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享95折优惠，另有部分特价房源；三期新品L14、L17号楼建面约106-139平房源在售</td>
                                    </tr>
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                                
                            
                        </table>
                        
                        <div class="btn-open">展开<i></i></div>
                        
                        </div>
                        
                        <div class="table-all" style="display: none;">
                            <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="110">记录时间</td>
                                <td width="90">均价</td>
                                <td width="90">起价</td>
                                <td width="342">价格描述</td>
                            </tr>
                             
                                <tr>
                                <td>2021-09-17</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享95折优惠，另有部分特价房源享受9折优惠～三期新品火爆热销中，欲购从速~</td>
                                </tr>
                            
                                <tr>
                                <td>2021-09-15</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享95折优惠，另有部分特价房源；优惠多多，先到先得～即将加推三期新品，敬请期待！</td>
                                </tr>
                            
                                <tr>
                                <td>2021-08-31</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享95折优惠，另有部分特价房源；三期新品L14、L17号楼建面约106-139平房源在售</td>
                                </tr>
                            
                                <tr>
                                <td>2021-08-31</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际L14、L17号楼已加推，建面约106-139平毛坯房源，备案均价约25444元/平；项目已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡</td>
                                </tr>
                            
                                <tr>
                                <td>2021-08-12</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享98折优惠，另有部分特价房源，优惠多多，先到先得~</td>
                                </tr>
                            
                                <tr>
                                <td>2021-08-11</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享98折优惠，另有部分特价房源，低至95折，先到先得～预计8月加推三期新品，70㎡起东湖复式正在诚意登记中</td>
                                </tr>
                            
                                <tr>
                                <td>2021-08-11</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享98折优惠，另有部分特价房源，先到先得～预计8月加推三期新品，70㎡起东湖复式正在诚意登记中</td>
                                </tr>
                            
                                <tr>
                                <td>2021-07-26</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享98折优惠，景观楼王L13号楼已加推，剩余少量房源在售.</td>
                                </tr>
                            
                                <tr>
                                <td>2021-07-23</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">L13号楼已于7月21日推出，主推建面约129、130平米毛坯高层，均价约26575元/平，目前尚有少量在售，前期少量建面约70-170㎡东湖复式/学府高层在售，单价约2.1-2.7万/㎡</td>
                                </tr>
                            
                                <tr>
                                <td>2021-07-20</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">L13号楼已拿预售证，即将推出，主推建面约129、130平米毛坯高层，备案均价约26575元/平，前期少量建面约70-170㎡东湖复式/学府高层在售，单价约2.1-2.7万/㎡</td>
                                </tr>
                            
                                <tr>
                                <td>2021-07-13</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分楼栋认购享98折优惠，另有部分95折特价房源在售。</td>
                                </tr>
                            
                                <tr>
                                <td>2021-07-05</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分房源认购可享98折优惠，另有部分特价房源在售，最高直降21万！</td>
                                </tr>
                            
                                <tr>
                                <td>2021-06-28</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分房源认购可享98折优惠，另有部分特价房源在售，最高直降21万！预计7月加推景观楼王新品.</td>
                                </tr>
                            
                                <tr>
                                <td>2021-06-15</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，认购可享98折优惠，还有少量一期特价房源在售，折后仅1.9万/㎡起，本月公寓样板间开放在即，敬请期待！</td>
                                </tr>
                            
                                <tr>
                                <td>2021-06-10</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分房源认购可享98折优惠，本月公寓样板间开放在即，公寓详情页即将上线，敬请期待！</td>
                                </tr>
                            
                                <tr>
                                <td>2021-06-03</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前主推建面约70-170㎡东湖复式/学府高层，单价约2.1-2.7万/㎡，部分房源认购可享98折优惠，即将推出新品，目前正在诚意登记中</td>
                                </tr>
                            
                                <tr>
                                <td>2021-06-02</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">主推建面约139-158平米洋房，毛坯备案均价约29933元/平，目前在售建面约115-170㎡景观高层，单价约2.1-2.7万/㎡，认购可享98折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2021-05-24</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前在售建面约115-170㎡东湖景观高层，单价约2.1-2.7万/㎡，认购可享98折优惠，即将加推最后一栋建面约140-160㎡低密墅质洋房，仅限12席</td>
                                </tr>
                            
                                <tr>
                                <td>2021-05-16</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前在售建面约115-170㎡东湖景观高层，单价约2.1-2.7万/㎡，认购可享98折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2021-05-10</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，目前在售建面约115-170㎡东湖景观高层，单价约2.1-2.7万/㎡，认购可享98折优惠，即将加推建面约140-160㎡绝版墅质洋房，仅限12席</td>
                                </tr>
                            
                                <tr>
                                <td>2021-05-06</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售建面约115-170㎡东湖景观高层，单价约2.1-2.7万/㎡，认购可享98折优惠，预计5月加推建面约140-160㎡墅质洋房</td>
                                </tr>
                            
                                <tr>
                                <td>2021-05-04</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售建面约115-170㎡东湖景观高层/墅质洋房，单价约2.1-2.7万/㎡，认购可享98折优惠.</td>
                                </tr>
                            
                                <tr>
                                <td>2021-04-30</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售建面约115-170㎡东湖景观高层/墅质洋房，单价约2.1-2.7万/㎡，5月1日即将加推新品，现已开启诚意登记，认购可享98折优惠，详情咨询售楼处</td>
                                </tr>
                            
                                <tr>
                                <td>2021-04-28</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">在售建面约115-170㎡东湖景观高层/墅质洋房，单价约2.1-2.7万/㎡，预计5月加推新品，现已开启诚意登记，认购可享98折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2021-04-25</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售建面约115-170㎡东湖景观高层/墅质洋房，单价约2.1-2.7万/㎡，预计5月加推新品，现已开启诚意登记，认购可享98折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2021-04-22</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">在售建面约115-170㎡东湖景观高层/墅质洋房，单价约2.1-2.7万/㎡，部分楼栋认购可享98折优惠，预计5月加推新品</td>
                                </tr>
                            
                                <tr>
                                <td>2021-04-02</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售L9、L12号楼建面约110-170㎡东湖景观高层，毛坯价格约21000元/平起，部分楼栋认购可享98折优惠，按时签约还有额外惊喜</td>
                                </tr>
                            
                                <tr>
                                <td>2021-03-29</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">L9、L12号楼已于3月27日推出，主推建面约115-170㎡东湖景观高层，毛坯价格21000元/平起，目前尚有少量在售，8、11号楼高层已拿预售证</td>
                                </tr>
                            
                                <tr>
                                <td>2021-03-23</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">10号楼建面约139-158平米毛坯洋房已推出，均价约27933元/平，开盘已售完，即将加推建面约115-170㎡东湖景观高层/墅质洋房，预计均价21000元/平起，诚意登记可享开盘98折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2021-03-20</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际即将加推建面约115-170㎡东湖景观高层/墅质洋房，预计均价21000元/平起，诚意登记可享开盘98折优惠，认购更有惊喜好礼。</td>
                                </tr>
                            
                                <tr>
                                <td>2021-03-18</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际即将加推建面约115-170㎡东湖景观高层/墅质洋房，诚意登记可享98折优惠，折后2万/平起，认购更有惊喜好礼。</td>
                                </tr>
                            
                                <tr>
                                <td>2021-03-10</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售L1、L3号楼少量建面约110-170平毛坯房源，价格21000元/平起</td>
                                </tr>
                            
                                <tr>
                                <td>2021-03-02</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际目前在售L1、L3号楼建面约110-170平毛坯房源，价格21000元/平起！</td>
                                </tr>
                            
                                <tr>
                                <td>2021-02-20</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售L1、L3号楼建面约110-170平毛坯房源，价格21000元/平起。</td>
                                </tr>
                            
                                <tr>
                                <td>2021-02-09</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际L1、L3号楼还剩少量建面约110-170平房源在售，价格21000元/平起.</td>
                                </tr>
                            
                                <tr>
                                <td>2021-01-12</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售L1、L3号楼建面约110-170平房源，价格21000元/平起，正在诚意登记中</td>
                                </tr>
                            
                                <tr>
                                <td>2021-01-02</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售L1、L3号楼建面约110-170平房源，价格2万元/平起</td>
                                </tr>
                            
                                <tr>
                                <td>2020-12-28</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售L1、L3号楼建面约110-170平房源，其中L3号楼价格2万元/平起，99折优惠将于12月31日截止；洋房Y10、Y15，正在诚意登记中</td>
                                </tr>
                            
                                <tr>
                                <td>2020-12-23</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际洋房Y10、Y15，正在登记中，24套洋房；目前在售L1、L3号楼建面约110-170平高层，其中L3号楼价格2万元/平起</td>
                                </tr>
                            
                                <tr>
                                <td>2020-12-09</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际洋房Y10、Y15，正在登记中，24套洋房；目前在售L1、L3号楼建面约110-170平高层，其中L3号楼价格2万元/平起</td>
                                </tr>
                            
                                <tr>
                                <td>2020-11-27</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际加推L1、L3号楼建面约110-170㎡高层房源，价格约20000元/㎡起</td>
                                </tr>
                            
                                <tr>
                                <td>2020-11-27</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际L3号楼建面约115、129平高层可直接认购，均价约22291元/平，L1号楼已拿预售即将推出，主推建面约122、141、169平高层，均价约25667元/平</td>
                                </tr>
                            
                                <tr>
                                <td>2020-11-26</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">L1、L3号楼高层已拿预售证，即将推出，主推L1号楼建面约122、141、169平高层，均价约25667元/平，以及L3号楼建面约115、129平高层，均价约22291元/平</td>
                                </tr>
                            
                                <tr>
                                <td>2020-11-16</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">在售少量建面约120-140㎡东湖景观高层房源，价格约20000元/平米起，即将加推L1、L3号楼</td>
                                </tr>
                            
                                <tr>
                                <td>2020-11-09</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售少量建面约120-140㎡东湖景观高层房源，价格约20000元/平米起，预计11月中旬加推L1、L3号楼，敬请关注！</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-30</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际L4号楼已拿预售证，已于10月29日推出，主推建面约106、129平米毛坯高层，均价约23500元/平，前期少量建面约120㎡东湖景观高层房源在售，价格约20000元/平米起</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-27</td>
                                <td> </td>
                                <td>约20000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际在售少量建面约120㎡东湖景观高层房源，价格约20000元/平米起，预计10月底加推L4号楼建面约106-130㎡毛坯房源</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-19</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">已于10月18日开盘推出L6号楼东湖景观高层，建面约119、138、165平米毛坯房源，价格约21000元/平米起，目前仅剩少量房源在售，预计10月底加推L4号楼</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-18</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际L6号楼已于10月18日开盘，主推建面约119、138、165平米毛坯房源，均价约24061元/平，价格约21000元/平米起，目前尚有少量房源在售</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-15</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际L6号楼高层已拿预售证，主推建面约119、138、165平米毛坯房源，备案均价约24061元/平，价格约21000元/平米起，目前正在认筹中，预计10月18日开盘</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-13</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">华侨城·欢乐天际将于10月18日首开L6号楼建面约100-170㎡东湖景观高层，毛坯价格预计21000元/平起</td>
                                </tr>
                            
                                <tr>
                                <td>2020-10-09</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">10月中旬首开L6号楼建面约100-170平米东湖景观高层房源，毛坯价格21000元/平起。</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-30</td>
                                <td> </td>
                                <td>约21000元/㎡</td>
                                <td class="td-left">9月26日首开洋房,当天售罄。高层预计21000元/平起，预计10月中旬开放</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-24</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际预计10月中旬推出景观高层毛坯房源，诚意登记可享开盘99折优惠！优惠截止日期为2020年10月15日</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-23</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际项目正在诚意登记中，诚意登记可享开盘99折优惠，预计9月首开建面约110-170平米高层/洋房，武汉高铁商务区城市展厅将于10月11日开放</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-16</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际9月即将首开推出建面约110-170㎡高层/洋房，已签约武汉小学，诚意登记可享开盘99折优惠，敬请关注！</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-09</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际，目前已签约武汉小学，9月即将首开推出建面约110-170㎡高层/洋房，诚意登记可享开盘99折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-03</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际已签约武汉小学，9月即将首开推出建面约110-170㎡高层/洋房，诚意登记可享开盘99折优惠</td>
                                </tr>
                            
                                <tr>
                                <td>2020-09-01</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际即将推出建面约110-170㎡高层、洋房，9月即将开盘，诚意登记可享开盘99折优惠，敬请关注</td>
                                </tr>
                            
                                <tr>
                                <td>2020-08-23</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际即将推出建面约110-170㎡高层、洋房</td>
                                </tr>
                            
                                <tr>
                                <td>2020-08-19</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际，项目预计9月首开，推出推建面约110-170㎡高层、洋房，敬请关注！</td>
                                </tr>
                            
                                <tr>
                                <td>2020-08-17</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际，位于武汉高铁商务区核心区，由广场区和中央区两大区域构成，广场区紧邻地铁4号线杨春湖站，中央区紧邻地铁4号线工业四路站，预计9月首开</td>
                                </tr>
                            
                                <tr>
                                <td>2020-08-11</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际，位于武汉高铁商务区核心区，由广场区和中央区两大区域构成，广场区紧邻地铁4号线杨春湖站，中央区紧邻地铁4号线工业四路站。敬请关注</td>
                                </tr>
                            
                                <tr>
                                <td>2020-07-08</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">欢乐天际中央区已签约武汉小学，即将推出建面约110-170㎡高层、洋房产品，价格待定，具体开盘时间待定</td>
                                </tr>
                            
                                <tr>
                                <td>2020-06-17</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">欢乐天际中央区已签约武汉小学，即将推出建面约110-170㎡高层、洋房产品，价格待定</td>
                                </tr>
                            
                                <tr>
                                <td>2020-04-02</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际首次开盘时间待定，价格待定</td>
                                </tr>
                            
                                <tr>
                                <td>2020-02-14</td>
                                <td> </td>
                                <td> </td>
                                <td class="td-left">华侨城·欢乐天际价格待定，首次开盘时间待定</td>
                                </tr>
                            
                        </table>
                        <div class="btn-off">收起<i></i></div>
                        </div>
                        
                    </div>
                </div>
                
                <!--价格信息结束-->
                
            </div>
            <!--左侧内容结束-->

            <!--右侧内容开始-->
            <div class="main-right">
                <link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/housevilla_xfcommon_active.css?v=202109160001" rel="stylesheet"/>
<!--20200903优惠活动-->
<div class="contenyh" style="display:none">
	<h3>优惠活动</h3>
	<div class="item_yh">
		<ul id="huodongList">			
		</ul>
	</div>
</div>
<!--20200903优惠活动  end-->

<!-- 获取优惠券 str -->
<div class="pop_box tf" style="display: none;" id="huodong_yhqform">
	<div class="pop_box_nr yhq">
		<div class="zc_header">
			<p style="line-height:66px;height:66px;">获取优惠券</p>
		</div>
		<div class="clearfix">
			<div class="fl left_cont mt38">
				<h4 class="gfyh">购房优惠券</h4>
				<div class="yh_sm">
					<p class="yhje" id="huodong_yhqform_money" style="font-size:20px;"></p>
					<p class="syjs" id="huodong_yhqform_youhui"></p>
				</div>
			</div>
			<div class="fl right_cont">
				<ul class="mt38">
					<li><span class="pr15">购房人:</span><input type="text" placeholder="输入真实姓名" class="tf" id="yhq_realname"></li>
					<li><span class="pr15">手机号:</span><input type="text" placeholder="输入手机号" class="tf" id="yhq_mobile"></li>
					<li id="yhq_authcode_box"><span class="pr15">验证码:</span><input id="yhq_authcode" type="text" value="验证码" class="check_m tf"><input type="button" value="获取验证码" class="hqyzm tf" id="yhq_verificationcode"></li>
					<li id="yhq_yanzhengma" style="display:none; width:267px;">
					</li>
				</ul>
			</div>
		</div>
	</div>
	<div class="yh_buy_finance" id="yhq_txd_div" style="display:none;">

	</div>
	<div class="zc_btn">
		<input class="tf cp ts_linear" type="button" value="立即申请" id="huodong_yhqform_baoming">
	</div>
	<!--div class="pop_box_clo" id="huodong_yhqform_close"><a href="javascript:void(0)"><img class="cls_bg" src="//static.soufunimg.com/zbs/newhouse/images/alf.gif " ></a></div-->
	<a class="newhouse_login_close" title="关闭" id="huodong_yhqform_close"><span></span></a>
</div>
<!--优惠券报名成功优惠码 begin-->
<div class="pop_box tf" style="display: none;" id="huodong_yhqres">
	<div class="pop_box_nr cyzc cur_lp">
		<div class="zc_header">
			<p>报名成功</p>
		</div>
		<div class="clearfix">
			<div class="fl yh_left_cont">
				<p class="tl f18 fb lh_24 cl_666 pb10">优惠<span id="huodong_yhqres_money"></span></p>
				<p class="f18" id="huodong_yhqres_time" style="font-size:15px;"></p>
				<p class="f24 yh_left_contp cl_666" style="font-size:22px;"><b id="huodong_yhqres_orderno">哈哈哈哈</b></p>
				<p class="f14" id="huodong_yhqres_youhui"></p>
				<p class="f14" id="huodong_yhqres_rules"></p>

			</div>
			<div class="fl yh_right_cont qr_box">
				<p class="qrdx" id="huodong_yhqres_sms">确认短信已发送至您<span id="huodong_yhqres_tele"></span>的手机，请注意查收，或在房天下-我的-优惠券中查看。</p>
			</div>
		</div>
	</div>
	<!--div class="pop_box_clo" id="huodong_yhqres_close"><a href="javascript:void(0)"><img class="cls_bg" src="//static.soufunimg.com/zbs/newhouse/images/alf.gif " ></a></div-->
	<a class="newhouse_login_close" title="关闭" id="huodong_yhqres_close"><span></span></a>
</div>
<!--优惠券领取失败 begin-->
<div class="pop_box tf" style="display: none;" id="huodong_yhqres_error1">
	<div class="pop_box_nr lqsb_header">
		<div class="zc_header">
			<p>领取失败</p>
		</div>
		<div class="lqsb_tsy">
			<p class="f24 cl_666">抱歉，此活动优惠券您已经领过！</p>
		</div>
	</div>
	<a class="newhouse_login_close" title="关闭" id="huodong_yhqres_error1_close"><span></span></a>
</div>
<!--优惠券抱歉 begin-->
<div class="pop_box tf" style="display: none;" id="huodong_yhqres_error2">
	<div class="pop_box_nr bq_header">
		<div class="zc_header">
			<p>领取失败,抱歉</p>
		</div>
		<div class="bq_tsy">
			<p class="f24 cl_666">您未抢到优惠券，请继续加油！</p>
		</div>
	</div>
	<div class="zc_btn">
		<input class="cp ts_linear tf" type="button" value="关闭" id="huodong_yhqres_error2_close1">
	</div>
	<!--div class="pop_box_clo" id="huodong_yhqres_error2_close"><a href="javascript:void(0)"><img class="cls_bg" src="//static.soufunimg.com/zbs/newhouse/images/alf.gif " ></a></div-->
	<a class="newhouse_login_close" title="关闭" id="huodong_yhqres_error2_close"><span></span></a>
</div>

<!--购房优惠券 end-->

<!--看房团报名弹窗 start-->
<div class="pop_bg pop_bg_signup" id="kft_div" style="display: none;">
    <div class="enroll_pop">
        <h3 class="popTitle">看房团报名</h3>
        <span class="close_enroll" id="huodong_kftform_close"></span>
        <div class="enroll_box clearfix">					
            <div class="enroll_leftlc" id="kft_enroll_leftlc" >
                <h4>报名流程</h4>
                <ul class="lc_kft">
                    <li class="icon_li1"><i></i>1.线上报名</li>
                    <li class="icon_li2"><i></i>2.电话确认</li>
                    <li class="icon_li3"><i></i>3.短信通知</li>
                    <li class="icon_li4"><i></i>4.案场看房</li>
                    <li class="icon_li5"><i></i>5.行程结束</li>
                </ul>
                <img src="//static.soufunimg.com/newhouse/images/kft/bus.gif" alt="" class="gif_car"/>
            </div>
            <div class="input_popbox">
                <p class="input_border"><span>手机号</span><input id="kft_mobile" type="text" name="" value="" placeholder="请输入手机号" class="wid250"/></p>
                <div class="input_yzm clearfix" id="kft_authcode_box">
                    <p class="input_border"><span>验证码</span><input id="kft_authcode" type="text" name="" value="" placeholder="请输入验证码" class="wid130"/></p>
                    <button class="btn_yzm" id="kft_verificationcode" >获取验证码</button>
                </div>
                <div id="kft_yanzhengma" class=""></div>
                <a href="javascript:void(0);" id="kft_submit" class="btn_build btn_red submitBtn">免费报名</a>
                <p class="agreement">
                    <label class="check-label"><input  id="kft_checkbox" type="checkbox" checked="true"><span class="check-box"></span>
                    我已阅读并同意<a href="https://passport.fang.com/Register/ServiceInfo" target="_blank">《房天下服务协议》</a><a href="http://my.fang.com/PrivacyPolicy/" target="_blank">《房天下隐私政策》</a>
                    </label>
                </p>
            </div>
        </div>
    </div>
</div>
<!--看房团报名弹窗 end-->
<!--201909专车看房报名弹窗-->
<div class="pop_bg" style="display:none;" id="zckf_div">
	<div class="enroll_pop">
		<h3>专车看房报名</h3>
		<span class="close_enroll" id="huodong_zckfform_close"></span>
		<div class="enroll_box clearfix">
			<div class="enroll_leftlc">
				<h4>报名流程</h4>
				<ul class="lc_zc">
					<li class="icon_li1"><i></i>1.线上报名</li>
					<li class="icon_li2"><i></i>2.客服确认</li>
					<li class="icon_li3"><i></i>3.专车上门</li>
					<li class="icon_li4"><i></i>4.案场看房</li>
					<li class="icon_li5"><i></i>5.专车返程</li>
				</ul>
				<img src="//static.soufunimg.com/newhouse/images/kft/car.gif" alt="" class="gif_car"/>
			</div>
			<div class="input_popbox">
				<p class="input_border"><span>手机号</span><input id="zckf_mobile" type="text" name="" value="" placeholder="请输入手机号" class="wid250"/></p>
				<div class="input_yzm clearfix" id="zckf_authcode_box">
					<p class="input_border"><span>验证码</span><input id="zckf_authcode"  type="text" name="" value="" placeholder="请输入验证码" class="wid130"/></p>
					<button class="btn_yzm" id="zckf_verificationcode">获取验证码</button>
				</div>
				<div class="" id="zckf_yanzhengma"></div>
				<a style="cursor:pointer;" id="zckf_submit" class="btn_build btn_red">免费报名</a>
			</div>
		</div>
	</div>
</div>
<!--报名成功-->
<div class="pop_bg pop_bg_suc" id="kf_suc" style="display:none;">
    <div class="enroll_pop wid500">
        <span class="close_enroll" id="kf_suc_close"></span>
        <h4 class="tit_cg"><span>恭喜您，报名成功！</span></h4>
        <div class="text_add">感谢您对房天下的关注，我们会尽快安排优质顾问/经纪人为您提供服务，为了您能及时了解看房团的最新消息，已将您加入到看房团群聊中，请下载房天下APP查看相关信息。
            <div class="icon_wen">
                <i onclick="javascript:window.open('http://newhouse.fang.com/house/2018-06-25/28798150.htm')"></i>
            </div>
        </div>
        <div class="clearfix ewm_dl">
            <dl>
                <dt>
                    
                        <img src="//img1.soufunimg.com/house/images/ewm_1703.png" alt="">
                    
                </dt>
                <dd>
                    <p></span></p>
                    <p></p>
                </dd>
            </dl>
            
        </div>
        <a class="newhouse_login_close" title="关闭" id="huodong_yhqform_close"><span></span></a> 
    </div>
</div>
<!--20191016报名弹窗-->
<div class="pop_bg" id="lptg_baoming_div" style="display: none;">
	<div class="enroll_pop wid600">
		<h3>团购报名</h3>
		<span class="close_enroll"></span>
		<div class="enroll_box clearfix">
			<div class="input_popbox">
				<p class="input_border"><span>手机号</span><input id="lptg_mobile" type="text" name="" value="" placeholder="请输入手机号" class="wid250"/></p>
				<div class="input_yzm clearfix" id="lptg_authcode_code">
					<p class="input_border"><span>验证码</span><input id="lptg_authcode" type="text" name="" value="" placeholder="请输入验证码" class="wid130"/></p>
					<button class="btn_yzm" id="lptg_verificationcode">获取验证码</button>
				</div>
				<div class="" id="lptg_yanzhengma" style="display:none;"></div>
				<a style="cursor:pointer;" id="lptg_submit" class="btn_build btn_red">免费报名</a>
				<p class="agreement">
					<label class="check-label"><input id="lptg_checkbox" type="checkbox" checked="true"><span class="check-box"></span>
					我已阅读并同意<a href="https://passport.fang.com/Register/ServiceInfo" target="_blank">《房天下服务协议》</a><a href="http://my.fang.com/PrivacyPolicy/" target="_blank">《房天下隐私政策》</a>
					</label>
				</p>
			</div>
		</div>
	</div>
</div>

<!--报名成功-->
<div class="pop_bg" id="lptg_success_div" style="display:none;">
	<div class="enroll_pop wid600">
		<span class="close_enroll"></span>
		<h4 class="tit_cg"><span>恭喜您，团购报名成功！</span></h4>
		<div class="text_add">
			<p>恭喜您！报名成功！</p>
			<p>团购成功后房天下会尽力跟开发商帮您争取最大幅度的优惠，如因特殊原因无法争取到本楼盘优惠时我们会为您推荐同类优惠楼盘，敬请期待！</p>
			<p>人多力量多！快去喊上亲朋好友一起团购吧！</p>
			
		</div>
		<div class="clearfix ewm_dl">
			
			<dl>
				<dt><img src="//imgwcs2.soufunimg.com/viewimage/house/2019_12/23/a3b4285f-c06b-43b4-b604-188fb5e47bc9/130x130.jpg" alt=""></dt>
				<dd>
					<p>微信扫码分享好友</p>
				</dd>
			</dl>
			
		</div>
	</div>
</div>

<!--预约看房弹窗 begin-->
<div class="pop_bg kfang" id="yykf_div" style="display: none;">
	<div class="enroll_pop">
		<h3>预约看房</h3>
		<span id="yykf_close" class="close_enroll"></span>
		<div class="enroll_box">
			<div class="enroll_leftlc">
				<h4>看房须知</h4>
				<p>前往售楼部看房请佩戴口罩，进入售楼部前将进行体温检测、洗手消毒和登记个人信息。根据要求，售楼部同时接待客户不能超过3组，如现场同时接待客户组数已满，请稍事等待。</p>
			</div>
			<div class="input_popbox">
			   <div class="input_border">
				<span>预约时间</span>
				<div class="choose date">
					<div id="dateSelectPoint" style="cursor:pointer;">
						<input style="cursor:pointer;" disabled="disabled" id="dateVal" type="text" placeholder="请选择日期">
						<i></i>
					</div>
					<ul id="dateSelect" data="date" class="selectUl" style="display:none;"></ul>
				</div>
				<div class="choose time">
					<div id="timeSelectPoint" style="cursor:pointer;">
						<input style="cursor:pointer;" disabled="disabled" date="time" id="timeVal" type="text" placeholder="请选择时间">
						<i></i>
					</div>
					<ul id="timeSelect"  class="selectUl"  style="display:none;"></ul>
				</div>
			   </div>
			   <div class="input_border">
				<span>预约人数</span>
				<div class="choose num">
					<div  id="personSelectPoint" >
						<input style="cursor:pointer;" type="text" id="personVal" disabled="disabled" placeholder="请选择人数" value='1人'>
						<i></i>
					</div>
					<ul id="peopleSelect"  class="selectUl"  style="display:none;">
						<li class="active">1人</li>
						<li>2人</li>
						<li>3人</li>
						<li>4人</li>
						<li>5人</li>
						<li>6人</li>
					</ul>
				</div>
			   </div>
			   <div class="input_border">
				<span>手机号</span>
				<input type="text" id="yykf_mobile" placeholder="输入手机号">
			   </div>
				<div id="yykf_authcode_box" class="input_border">
					<span>验证码</span>
					<input  id="yykf_authcode" type="text" placeholder="输入验证码">
					<a id="yykf_verificationcode" class="btn-yzm">获取验证码</a>
				</div>
				<div id="yykf_yanzhengma" style="display:none;"></div>
				<a style="cursor:pointer;" id="yykf_submit" class="btn_build btn_red">立即预约</a>
				<p class="agreement"><label class="check-label"><input type="checkbox" id="yykf_checkbox" ><span class="check-box"></span>
					我已阅读并同意<a href="https://passport.fang.com/Register/ServiceInfo" target="_blank">《房天下服务协议》</a>
								  <a href="http://my.fang.com/PrivacyPolicy/" target="_blank">《房天下隐私政策》</a></label>
				</p>
		</div>
		</div>
	</div>
</div>
<!--预约看房弹窗 end-->
<!--预约成功弹窗 begin-->
<div class="pop_bg kfang" id="yykf_success" style="display:none;">
	<div class="enroll_pop wid500">
			<span class="close_enroll" id="yykf_success_close"></span>
			<h3 class="lp">华侨城·欢乐天际</h3>
			<h4 class="tit_cg"><span>恭喜您，报名成功！</span></h4>
			<div class="text_add">
				<p class="text-center">感谢您对房天下的关注，置业顾问会尽快联系您为您提供服务。</p>
			</div>
			<div class="clearfix ewm_dl">
				<dl>
					<dt><img src="//static.soufunimg.com/newhouse/images/newhouse/qrcode0129.jpg" alt=""></dt>
					<dd>
						<p>下载<em>房天下APP</em><br>随时查看预约房源</p>
					</dd>
				</dl>
			</div>
		</div>
</div>
<!--预约成功弹窗 end-->
<!--预约失败弹窗 begin-->
<div class="pop_bg kfang" id="yykf_error"  style="display: none;">
	<div class="enroll_pop wid500">
		<span class="close_enroll" id="yykf_error_close"></span>
		<h3 class="lp">华侨城·欢乐天际</h3>
		<h4 class="tit_err"><span>很抱歉，预约失败！</span></h4>
		<div class="text_add">
			<p>感谢您对房天下的关注。可能网络超时，请稍后重试。您也可以下载房天下APP进行预约。</p>
		</div>
		<div class="clearfix ewm_dl">
			<dl>
				<dt><img src="//static.soufunimg.com/newhouse/images/newhouse/qrcode0129.jpg" alt=""></dt>
				<dd>
					<p>下载<em>房天下APP</em><br>随时预约看房</p>
				</dd>
			</dl>
		</div>
	</div>
</div>
<!--预约失败弹窗 end-->

                
                <!--201903导购-->
                <dl class="news-window mt12">
                    <dt class="clears">
                        <span class="djdk">相关导购</span>
                        <a href="//wuhan.newhouse.fang.com/house/daogou/index.htm" class="more-news">更多&gt;&gt;</a>
                    </dt>
                    <dd style="padding: 8px 0;">
                        
                        <div class="inf-line clearfix">
                            <i class="inf-numb top-num">1</i>
                            <span class="inf-tit"><a href="https://wuhan.newhouse.fang.com/2021-07-15/40699296.htm" target="_blank" title="查看华侨城·欢乐天际靠谱人气置业顾问!">查看华侨城·欢乐天际靠谱人气置业顾问!</a></span>
                        </div>
                        
                        <div class="inf-line clearfix">
                            <i class="inf-numb top-num">2</i>
                            <span class="inf-tit"><a href="https://wuhan.newhouse.fang.com/2021-08-22/41219106.htm" target="_blank" title="华侨城·欢乐天际新拍短视频,实时了解楼盘新动态!">华侨城·欢乐天际新拍短视频,实时了解楼盘新动态!</a></span>
                        </div>
                        
                        <div class="inf-line clearfix">
                            <i class="inf-numb top-num">3</i>
                            <span class="inf-tit"><a href="https://wuhan.newhouse.fang.com/2021-09-12/41448754.htm" target="_blank" title="华侨城·欢乐天际新拍现场图片,实时了解楼盘新动态!">华侨城·欢乐天际新拍现场图片,实时了解楼盘新动态!</a></span>
                        </div>
                        
                        <div class="inf-line clearfix">
                            <i class="inf-numb ">4</i>
                            <span class="inf-tit"><a href="https://wuhan.newhouse.fang.com/2021-09-13/41469725.htm" target="_blank" title="从华侨城·欢乐天际现场发来一条项目新消息,请查看!">从华侨城·欢乐天际现场发来一条项目新消息,请查看!</a></span>
                        </div>
                        
                        <div class="inf-line clearfix">
                            <i class="inf-numb ">5</i>
                            <span class="inf-tit"><a href="https://www.fang.com/daogou/xf-wuhan-39968387.html" target="_blank" title="武汉华侨城·欢乐天际怎么样?看小区户型观房价走势买好房">武汉华侨城·欢乐天际怎么样?看小区户型观房价走势买好房</a></span>
                        </div>
                        
                    </dd>
                </dl>
                <!--导购end-->
                
                <!--帮你找房开始-->
                <!--新房委托入口 start-->
<link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/common/entrust_entrance.css?v=202109160001" rel="stylesheet"/>
<div class="zf-help"  style="margin-bottom: 20px;" >
	<h2 class="" style="height: 40px;line-height 40px;"><span>帮你找房</span></h2>
	<ul style="padding: 20px 0 18px; width: 278px;" >
		<li class="fm-line clearfix" id="entrust_district_li">
			<label for="" class="fl zf-lab">意向区域：</label>
			<div class="zf-select fl" style="z-index: 1000;">
				<i class="s-arr"></i>
				<span class="mr-opn" id="entrust_district">不限</span>
				<ul class="zf-opns" id="district_list">
                    
                        <li class="zf-opn">东湖高新区</li>
                    
                        <li class="zf-opn">洪山</li>
                    
                        <li class="zf-opn">江岸</li>
                    
                        <li class="zf-opn">东西湖</li>
                    
                        <li class="zf-opn">汉阳</li>
                    
                        <li class="zf-opn">武昌</li>
                    
                        <li class="zf-opn">江汉</li>
                    
                        <li class="zf-opn">经济开发区</li>
                    
                        <li class="zf-opn">硚口</li>
                    
                        <li class="zf-opn">黄陂</li>
                    
                        <li class="zf-opn">江夏</li>
                    
                        <li class="zf-opn">青山</li>
                    
                        <li class="zf-opn">蔡甸</li>
                    
                        <li class="zf-opn">新洲</li>
                    
                        <li class="zf-opn">汉南</li>
                    
                        <li class="zf-opn">其他</li>
                    
                        <li class="zf-opn">武汉周边</li>
                    
				</ul>
			</div>
		</li>
		<!--20180312  start-->
		<li class="fm-line clearfix" id="yxloupan_container">
			<label for="" class="fl zf-lab">意向楼盘：</label>
			<div class="fl">
				<div id='yxlptuijian' style='display:none;'>
					
				</div>
				<input type="text" class="zf-input" id="yxloupan"  placeholder="请选择您的意向楼盘" style="color: rgb(102, 102, 102);" autocomplete="off"/>
				<input type="hidden" id="entrust_projname"/>
				<input type="hidden" id="entrust_newcode"/>
			</div>

            <div class="clear"></div>
		</li>
		<!--20180312  end-->
		
		<li class="fm-line clearfix" id="entrust_price_li">
			<label for="" class="fl zf-lab">预算总价：</label>
			<div class="zf-select fl">
				<i class="s-arr"></i>
				<span class="mr-opn" id="entrust_price">不限</span>
				<ul class="zf-opns" id="price_list">
                        
                        <li class="zf-opn">10000已下</li>
                        
                        <li class="zf-opn">10000-15000</li>
                        
                        <li class="zf-opn">15000-20000</li>
                        
                        <li class="zf-opn">20000-25000</li>
                        
                        <li class="zf-opn">30000已上</li>
                        
				</ul>
			</div>
		</li>
		<li class="fm-line clearfix">
			<label for="" class="fl zf-lab">手机号码：</label>
			<input type="text" class="zf-input" autocomplete="off" id="entrust_mobile"/>
		</li>
		<!--图形验证-->
		<li id="entrust_yanzhengma" class='clearfix' style="margin-bottom:10px;display:none;"></li>
		<li class="fm-line clearfix">
			<label for="" class="fl zf-lab">验<i style="margin-left: 7px;"></i>证<i style="margin-left: 7px;"></i>码：</label>
			<input type="text" class="zf-input fl" style="width: 82px;margin-right: 10px;" id="entrust_authcode"/>
			<input type="button" class="yz-btn fl" value="发送验证码" href="javascript:void(0);"  id="entrust_verificationcode"/>
		</li>
		<li style="margin-top: 10px;"><input type="button" class="zf-sub" value="提交" id="entrust_submit"/></li>
		<li style="margin-top: 10px;font-size:12px;color:#999"><input type="checkbox" checked="checked" id="huodong_bnmf_check" style="vertical-align:middle;">我已经看过并同意<a href="https://passport.fang.com/Register/ServiceInfo" target="_blank">《房天下服务协议》</a><a href="http://my.fang.com/PrivacyPolicy/" target="_blank">《房天下隐私权政策》</a></li>
	</ul>

</div>
<div class="tj-pop" id="entrust_success" style="display:none;">
	<div class="mask"></div>
	<div class="tj-result">
		<i class="tj-close" id="entrust_success_close"></i>
		<div class="tj-result-top">
			<i class="cg-ic"></i>
			<h4 class="tjg">提交成功!</h4>
			<h5 class="jgxq">感谢您对房天下的关注，房天下顾问会尽快与您联系。</h5>
			<div class="clear"></div>
		</div>
		<div class="tj-result-bot">
			<p class="lp-interest">您可能感兴趣的楼盘</p>
			<ol id='tjList'>				
			</ol>
		</div>
	</div>
</div>


 <div class="tj-pop" id="entrust_failed" style="display:none;">
	<div class="mask"></div>
	<div class="tj-result">
		<i class="tj-close" id="entrust_failed_close"></i>
		<i class="fal-ic"></i>
		<h4 class="tjg" style="top: 100px;left: 230px;">提交失败</h4>
		<h5 class="jgxq">信息填写不完整，请检查后再提交！</h5>
	</div>
</div>
<!--新房委托入口 end-->
                <!--帮你找房结束-->
                <!--周边楼盘开始-->
                
                <div id="sjina_C13_08" class="contentHot">
                    <h3 ctm-data="rmlp_bt" class="clearfix">
                        周边楼盘
                    </h3>
                    <div ctm-data="rmlp_lb" id="sjina_D10_03" class="hotContent">
                        <dl>
                            <dt class="clearfix">
                                <span class="mc">楼盘名称</span><span class="jg">价格</span><span class="lt">论坛</span>
                            </dt>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://donghuchengfxhy.fang.com/" target="_blank">福星惠誉东湖城</a></span>
                                    <span class="jg"><b>15000</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2611099466/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://baolichengsohozhongxin.fang.com/" target="_blank">保利城SOHO中心</a></span>
                                    <span class="jg"><b>12500</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2611093236/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://nuozhanxingzuo.fang.com/" target="_blank">诺展星座</a></span>
                                    <span class="jg"><b>20000</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2610153106/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://39dajiezy.fang.com/" target="_blank">中冶·39大街</a></span>
                                    <span class="jg"><b>24615</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2610153702/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://binjiangzhongxinlt.fang.com/" target="_blank">联泰外滩领馆</a></span>
                                    <span class="jg"><b>12388</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2611121234/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://yijiangjingchengzs.fang.com/" target="_blank">招商一江璟城</a></span>
                                    <span class="jg"><b>21212</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2610153928/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://donghujinmaofu.fang.com/" target="_blank">东湖金茂府</a></span>
                                    <span class="jg"><b>22000</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board/2610154032/" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://jinmaoguojigongyu.fang.com/" target="_blank">金茂国际公寓</a></span>
                                    <span class="jg"><b>20000</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board//" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://fangyuan.fang.com/" target="_blank">方园</a></span>
                                    <span class="jg"><b>19800</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board//" target="_blank">BBS</a></span>
                                </dd>
                            
                                <dd class="clearfix">
                                    <span class="mc"><a href="http://linhuyifang.fang.com/" target="_blank">邻湖壹方</a></span>
                                    <span class="jg"><b>18000</b>元/㎡</span>
                                    <span class="lt"><a href="http://wuhan.bbs.fang.com/board//" target="_blank">BBS</a></span>
                                </dd>
                            
                        </dl>
                    </div>
                </div>
                
                <!--周边楼盘结束-->
                <!--同价位楼盘开始-->
                
                <div id="sjina_C13_08" class="contentHot">
                    <h3 ctm-data="rmlp_bt" class="clearfix">
                        同价位楼盘
                    </h3>
                    <div ctm-data="rmlp_lb" id="sjina_D10_03" class="hotContent">
                        <dl>
                            <dt class="clearfix">
                                <span class="mc">楼盘名称</span><span class="jg">价格</span><span class="lt">区县</span>
                            </dt>
                            
                                <dd class="clearfix">
                                <a href="http://wudihanyangyinxiang.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">武汉城建汉阳印象</span>
                                        
                                            <span class="jg"><b>21000</b>元/㎡</span>
                                        
                                        <span class="lt">汉阳</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://meilianchengguan.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">美联城观</span>
                                        
                                            <span class="jg"><b>20606</b>元/㎡</span>
                                        
                                        <span class="lt">江岸</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://huanletianjihqc.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">华侨城·欢乐天际</span>
                                        
                                            <span class="jg"><b>21000</b>元/㎡</span>
                                        
                                        <span class="lt">洪山</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://hanjiangwanxsj.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">万科新世纪翡翠滨江</span>
                                        
                                            <span class="jg"><b>20850</b>元/㎡</span>
                                        
                                        <span class="lt">汉阳</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://jiangshanheyuezs.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">招商江山和樾</span>
                                        
                                            <span class="jg"><b>20896</b>元/㎡</span>
                                        
                                        <span class="lt">汉阳</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://fengqitinglanlcjd.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">绿城金地凤起听澜</span>
                                        
                                            <span class="jg"><b>21000</b>元/㎡</span>
                                        
                                        <span class="lt">汉阳</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://aoyuanbinjiangguoji.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">奥园滨江国际</span>
                                        
                                            <span class="jg"><b>20500</b>元/㎡</span>
                                        
                                        <span class="lt">青山</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://hzwgzyst.fang.com/villa/" class="clearfix" target="_blank">
                                        <span class="mc">华中文谷知音盛棠</span>
                                        
                                            <span class="jg"><b>21000</b>元/㎡</span>
                                        
                                        <span class="lt">蔡甸</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://guangguyuecheng.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">光谷悦城</span>
                                        
                                            <span class="jg"><b>20500</b>元/㎡</span>
                                        
                                        <span class="lt">东湖高新区</span>
                                    </a>
                                </dd>
                            
                                <dd class="clearfix">
                                <a href="http://lingjiaohuyihaoyh.fang.com/" class="clearfix" target="_blank">
                                        <span class="mc">禹洲菱角湖壹号</span>
                                        
                                            <span class="jg"><b>21000</b>元/㎡</span>
                                        
                                        <span class="lt">江汉</span>
                                    </a>
                                </dd>
                            
                        </dl>
                    </div>
                </div>
                
                <!--同价位楼盘结束-->
            </div>
            <!--右侧内容结束-->
        </div>
        <!--内容区结束-->
    </div>
    </div>
	<!--主体内容 end-->
<div class="clear10"></div>
<link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/common/bottom_inlink.css?v=202109160001" rel="stylesheet"/>
<!--20181126SEO内链begin-->
<div class="near_estate">
	<div class="bigtit0307 clearfix">
		<!--推荐楼盘-->
		
		<div class="s1"  id="tab_phb_1" >
			<a class='tab' href="javascript:void(0)" data="1" >推荐楼盘</a>
		</div>
		
		<!--热门楼盘-->
		
        <div class="s2"  id="tab_phb_2">
			<a class='tab' href="javascript:void(0)" data="2" >热门楼盘</a>
		</div>
		
		<!--最新楼盘-->
		
        <div class="s2"  id="tab_phb_3">
			<a class='tab' href="javascript:void(0)" data="3" >最新楼盘</a>
		</div>
		
		<!--附近楼盘-->
		
        <div class="s2"  id="tab_phb_4">
			<a class='tab' href="javascript:void(0)" data="4" >附近楼盘</a>
		</div>
		
		<!--商圈楼盘-->
		
		<div class="s2"  id="tab_phb_5">
			<a class='tab' href="javascript:void(0)" data="5" >商圈楼盘</a>
		</div>
		
		<!--综合推荐-->
		<div class="s2"  id="tab_phb_6">
			<a class='tab' href="javascript:void(0)" data="6" >综合推荐</a>
		</div>
		<span style="float:right;font-size:12px;font-weight:normal;padding-right:10px;">如果您想找的楼盘我们还未收录，您可以<a id="ls_pop_show" style="color:#f33" ctm-data-idx="1" href="javascript:void(0);">提交给我们</a></span>
	</div>
	
	<!--楼盘推荐-->
	<div class="nhbox content_phb_1">
		<ul class="hotlptj fjlp">
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511762071/housedetail.htm" title="富力城 五星名座" target="_blank">富力城 五星名座</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138027/housedetail.htm" title="中海·河山郡" target="_blank">中海·河山郡</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138071/housedetail.htm" title="澜湖·璞园" target="_blank">澜湖·璞园</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138765/housedetail.htm" title="万科翡翠都会" target="_blank">万科翡翠都会</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138791/housedetail.htm" title="包头恒大学府" target="_blank">包头恒大学府</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138831/housedetail.htm" title="金地风华九里" target="_blank">金地风华九里</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511718147/housedetail.htm" title="正翔国际" target="_blank">正翔国际</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138741/housedetail.htm" title="万科公园五号" target="_blank">万科公园五号</a></li>
			
			<li><a href="https://bt.newhouse.fang.com/loupan/1511138245/housedetail.htm" title="碧桂园·凤凰天域" target="_blank">碧桂园·凤凰天域</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313684129/housedetail.htm" title="朝阳花园" target="_blank">朝阳花园</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313187875/housedetail.htm" title="卓正上东区" target="_blank">卓正上东区</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313189085/housedetail.htm" title="鸿坤·理想尔湾" target="_blank">鸿坤·理想尔湾</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313195351/housedetail.htm" title="鹏渤·印象城" target="_blank">鹏渤·印象城</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313196039/housedetail.htm" title="上河·天著" target="_blank">上河·天著</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313196647/housedetail.htm" title="华都名晟" target="_blank">华都名晟</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313196683/housedetail.htm" title="泽润·锦绣名门" target="_blank">泽润·锦绣名门</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313197283/housedetail.htm" title="宏昌园东区" target="_blank">宏昌园东区</a></li>
			
			<li><a href="https://bd.newhouse.fang.com/loupan/1313197301/housedetail.htm" title="爱情城" target="_blank">爱情城</a></li>
			
			<li><a href="https://bh.newhouse.fang.com/loupan/2913198004/housedetail.htm" title="北海恒大雅苑" target="_blank">北海恒大雅苑</a></li>
			
			<li><a href="https://bh.newhouse.fang.com/loupan/2913198758/housedetail.htm" title="融创海映长滩" target="_blank">融创海映长滩</a></li>
			
		</ul>
	</div>
	
	
	<!--热门楼盘-->
	<div class="nhbox content_phb_2"  style="display:none;">
		<ul class="hotlptj fjlp">
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2611027702/housedetail.htm" title="华中智谷" target="_blank">华中智谷</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158476/housedetail.htm" title="华侨城·红坊" target="_blank">华侨城·红坊</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155102/housedetail.htm" title="华生城·首府" target="_blank">华生城·首府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154530/housedetail.htm" title="新华尚水湾" target="_blank">新华尚水湾</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154990/housedetail.htm" title="新影华翔城" target="_blank">新影华翔城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154984/housedetail.htm" title="新华壹号" target="_blank">新华壹号</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2611243346/housedetail.htm" title="华发中城荟" target="_blank">华发中城荟</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155772/housedetail.htm" title="华发四季" target="_blank">华发四季</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154872/housedetail.htm" title="华发峰尚" target="_blank">华发峰尚</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610153534/housedetail.htm" title="华中城" target="_blank">华中城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610159286/housedetail.htm" title="华润瑞府" target="_blank">华润瑞府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610159098/housedetail.htm" title="盘龙华府" target="_blank">盘龙华府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610153456/housedetail.htm" title="龙庭华府" target="_blank">龙庭华府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158450/housedetail.htm" title="东兴华庭" target="_blank">东兴华庭</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156430/housedetail.htm" title="交投华园" target="_blank">交投华园</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156162/housedetail.htm" title="荣盛华庭" target="_blank">荣盛华庭</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155574/housedetail.htm" title="洺悦华府" target="_blank">洺悦华府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610153400/housedetail.htm" title="泷悦华府" target="_blank">泷悦华府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610153890/housedetail.htm" title="华润桃源里商铺" target="_blank">华润桃源里商铺</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156836/housedetail.htm" title="华生新城·国土郡" target="_blank">华生新城·国土郡</a></li>
			
		</ul>
	</div>
	
	
	<!--最新楼盘-->
	<div class="nhbox content_phb_3"  style="display:none;">
		<ul class="hotlptj fjlp">
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610161826/housedetail.htm" title="保利·青年荣耀" target="_blank">保利·青年荣耀</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610159094/housedetail.htm" title="蓝城·湖畔雲境" target="_blank">蓝城·湖畔雲境</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158922/housedetail.htm" title="城投墨北璟苑" target="_blank">城投墨北璟苑</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158908/housedetail.htm" title="武汉卓越城" target="_blank">武汉卓越城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158906/housedetail.htm" title="金湖听语四期住宅" target="_blank">金湖听语四期住宅</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158520/housedetail.htm" title="江印" target="_blank">江印</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158474/housedetail.htm" title="南德缦和世纪" target="_blank">南德缦和世纪</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610157034/housedetail.htm" title="长投·航空路壹号·璞寓" target="_blank">长投·航空路壹号·璞寓</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156786/housedetail.htm" title="武汉城建汉阳印象" target="_blank">武汉城建汉阳印象</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156738/housedetail.htm" title="武汉青创城" target="_blank">武汉青创城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156686/housedetail.htm" title="金茂华发武汉国际社区" target="_blank">金茂华发武汉国际社区</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156654/housedetail.htm" title="美联城观" target="_blank">美联城观</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156536/housedetail.htm" title="中粮祥云地铁小镇" target="_blank">中粮祥云地铁小镇</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156404/housedetail.htm" title="佳阳大都府" target="_blank">佳阳大都府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156368/housedetail.htm" title="汉津阳光城" target="_blank">汉津阳光城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156134/housedetail.htm" title="武汉城建·电建|君樾府" target="_blank">武汉城建·电建|君樾府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156074/housedetail.htm" title="绿城·尊蓝" target="_blank">绿城·尊蓝</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156026/housedetail.htm" title="大华锦绣时代" target="_blank">大华锦绣时代</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155954/housedetail.htm" title="地铁时代云上城" target="_blank">地铁时代云上城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154720/housedetail.htm" title="滨江金茂府" target="_blank">滨江金茂府</a></li>
			
		</ul>
	</div>
	
	
	<!--附近楼盘-->
	<div class="nhbox content_phb_4" style="display:none;">
		<ul class="hotlptj fjlp">
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156494/housedetail.htm" title="华侨城·欢乐天际" target="_blank">华侨城·欢乐天际</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610159024/housedetail.htm" title="万科东湖堤白" target="_blank">万科东湖堤白</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154032/housedetail.htm" title="东湖金茂府" target="_blank">东湖金茂府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155084/housedetail.htm" title="金茂国际公寓" target="_blank">金茂国际公寓</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156950/housedetail.htm" title="杨春湖畔·境寓" target="_blank">杨春湖畔·境寓</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156008/housedetail.htm" title="邻湖壹方" target="_blank">邻湖壹方</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2611262142/housedetail.htm" title="金地自在城金地广场商业街" target="_blank">金地自在城金地广场商业街</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154066/housedetail.htm" title="金科城" target="_blank">金科城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2611099466/housedetail.htm" title="福星惠誉东湖城" target="_blank">福星惠誉东湖城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156670/housedetail.htm" title="铁投邻里荟" target="_blank">铁投邻里荟</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155110/housedetail.htm" title="铁投邻里荟商铺" target="_blank">铁投邻里荟商铺</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155700/housedetail.htm" title="方园" target="_blank">方园</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158980/housedetail.htm" title="保利云上" target="_blank">保利云上</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156050/housedetail.htm" title="奥园滨江国际" target="_blank">奥园滨江国际</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155060/housedetail.htm" title="印力中心" target="_blank">印力中心</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156026/housedetail.htm" title="大华锦绣时代" target="_blank">大华锦绣时代</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158976/housedetail.htm" title="青扬港厦" target="_blank">青扬港厦</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156600/housedetail.htm" title="武汉城建·融创|和平中心" target="_blank">武汉城建·融创|和平中心</a></li>
			
		</ul>
	</div>
	
	
	<!--商圈楼盘-->
	<div class="nhbox content_phb_5"  style="display:none;">
		<ul class="hotlptj fjlp">
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610159094/housedetail.htm" title="蓝城·湖畔雲境" target="_blank">蓝城·湖畔雲境</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158908/housedetail.htm" title="武汉卓越城" target="_blank">武汉卓越城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154032/housedetail.htm" title="东湖金茂府" target="_blank">东湖金茂府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156494/housedetail.htm" title="华侨城·欢乐天际" target="_blank">华侨城·欢乐天际</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155788/housedetail.htm" title="南益名悦华府" target="_blank">南益名悦华府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154276/housedetail.htm" title="美好长江首玺" target="_blank">美好长江首玺</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156528/housedetail.htm" title="中建壹品宏泰·阅江府" target="_blank">中建壹品宏泰·阅江府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156518/housedetail.htm" title="城投联投江南岸" target="_blank">城投联投江南岸</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155998/housedetail.htm" title="万科新都会" target="_blank">万科新都会</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610155038/housedetail.htm" title="旭辉江山境" target="_blank">旭辉江山境</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154638/housedetail.htm" title="旭辉华宇江悦府" target="_blank">旭辉华宇江悦府</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610154552/housedetail.htm" title="新力城" target="_blank">新力城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158980/housedetail.htm" title="保利云上" target="_blank">保利云上</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610158928/housedetail.htm" title="诚功新时代" target="_blank">诚功新时代</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156634/housedetail.htm" title="万科城市之光" target="_blank">万科城市之光</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156482/housedetail.htm" title="锦绣江城" target="_blank">锦绣江城</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156270/housedetail.htm" title="旭辉都会山" target="_blank">旭辉都会山</a></li>
			
			<li><a href="https://wuhan.newhouse.fang.com/loupan/2610156230/housedetail.htm" title="万科保利理想城市" target="_blank">万科保利理想城市</a></li>
			
		</ul>
	</div>
	
	<!--综合推荐-->
	<div class="nhbox content_phb_6"  style="display:none;">
		<ul class="hotlptj fjlp">
			<li><a href="//wuhan.newhouse.fang.com/house/s/" title="武汉新房" target="_blank">武汉新房</a></li>
			<li><a href="//fangjia.fang.com/pghouse-c0wuhan/h315-s11/" title="武汉小区" target="_blank">武汉小区</a></li>
			<li><a href="//wuhan.esf.fang.com/" title="武汉二手房" target="_blank">武汉二手房</a></li>
			<li><a href="//wuhan.zu.fang.com/" title="武汉租房" target="_blank">武汉租房</a></li>
			<li><a href="//wuhan.home.fang.com/" title="武汉装修" target="_blank">武汉装修</a></li>
			<li><a href="//home.fang.com/dianpu/wuhan/" title="武汉装修公司" target="_blank">武汉装修公司</a></li>
			<li><a href="//fangjia.fang.com/wuhan/" title="武汉房价" target="_blank">武汉房价</a></li>
			<li><a href="//wuhan.office.fang.com/" title="武汉写字楼" target="_blank">武汉写字楼</a></li>
			<li><a href="//wuhan.shop.fang.com/" title="武汉商铺" target="_blank">武汉商铺</a></li>
			<li><a href="//wuhan.news.fang.com/" title="武汉房产资讯" target="_blank">武汉房产资讯</a></li>
			<li><a href="//wuhan.newhouse.fang.com/house/kanfangtuan.htm" title="武汉看房团" target="_blank">武汉看房团</a></li>
			<li><a href="//wuhan.bbs.fang.com/" title="武汉业主论坛" target="_blank">武汉业主论坛</a></li>
			<li><a href="//wuhan.newhouse.fang.com/entrust/" title="武汉楼盘" target="_blank">武汉楼盘</a></li>
			<li><a href="//fdc.fang.com/" title="产业网" target="_blank">产业网</a></li>
			<li><a href="//world.fang.com/" title="海外房产" target="_blank">海外房产</a></li>
			<li><a href="//newhouse.fang.com/house/tools.htm" title="房贷计算器" target="_blank">房贷计算器</a></li>
			<li><a href="//zhishi.fang.com/" title="房产知识" target="_blank">房产知识</a></li>
			<li><a href="//www.fang.com/ask/" title="房产问答" target="_blank">房产问答</a></li>
		</ul>
	</div>
</div>
<!--20181126SEO内链end-->
 <link href="//static.soufunimg.com/newhouse/style/loupanSubmit.css?v=1202109160001" type="text/css" rel="stylesheet">
<link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/webuploader.css?v=202109160001" rel="stylesheet" />
<div id="ls_pop_box" class="formwrapopen" style="display: none;z-index: 10000 !important;">
    <div class="opendiv">
        <div style="height:600px;overflow-x:hidden;overflow-y:auto">
        <a id="ls_pop_close" class="close" href="javascript:void(0);"></a>
        <div class="formwrap">
            <dl>
                <dt><i>*</i>楼盘名称</dt>
                <dd><input id="ls_pop_projName" value="" placeholder="请输入楼盘名" name="" class="intext w1"><em>限20个字</em>
                    <span>楼盘别名</span><input id="ls_pop_nickName" value="" placeholder="请输入楼盘别名" name=""
                                            class="intext w2"><em>多个用，隔开</em>
                </dd>
            </dl>
            <dl>
                <dt><i>*</i>楼盘地址</dt>
                <dd>
                    <div class="seldiv">
                        <p id="ls_pop_showDistrict" class="select"><input id="ls_pop_district" type="" value="" placeholder="请选择" name="" class="intext w4"><i></i></p>
                        <ul id="ls_pop_disBox" class="option none">



                        </ul>
                    </div>
                    <div id="ls_pop_comSec" class="seldiv mal10">
                        <p id="ls_pop_showComarea" class="select wli5"><input id="ls_pop_comarea" type="" value="" placeholder="请选择" name="" class="intext w5"><i></i>
                        </p>
                        <ul id="ls_pop_comBox" class="option none">
                            <li class="wli5">请选择</li>
                        </ul>
                    </div>
                    <input id="ls_pop_address" value="" placeholder="请输入地址" name="" class="intext w3 mal10">
                </dd>
            </dl>
            <dl>
                <dt><i></i>您的称呼</dt>
                <dd><input id="ls_pop_name" value="" placeholder="姓名" name="" class="intext w4a"></dd>
                <a id="ls_pop_showMore" class="brn_stop" href="javascript:void(0);">更多信息<img
                        src="//img1.soufunimg.com/house/images/search/btn01.png" width="11" height="6"/></a>
            </dl>
            <div id="ls_pop_moreInfo" style="display: none;">
                
                <dl>
                    <dt><i></i>环线位置</dt>
                    <dd>
                        <div class="seldiv">
                            <p id="ls_pop_showRound" class="select">
                                <input id="ls_pop_round" type="" value="" placeholder="请选择" name="" class="intext w4"><i></i>
                            </p>
                            <ul id="ls_pop_roundBox" class="option none">
                                
                                    <li>内环以内</li>
                                
                                    <li>内至二环</li>
                                
                                    <li>二至中环</li>
                                
                                    <li>中环以外</li>
                                 
                            </ul>
                        </div>
                    </dd>
                </dl>
                
                <dl>
                    <dt><i></i>建筑类型</dt>
                    <dd id="ls_pop_BuildCategorys">
                        <span class="chdiv">板楼</span>
                        <span class="chdiv mal10">塔楼</span>
                        <span class="chdiv mal10">板塔结合</span>
                        <em>可单选，也可复选</em>
                    </dd>
                </dl>
                <dl>
                    <dt><i></i>建筑楼层</dt>
                    <dd id="ls_pop_BuildingForm">
                        <span class="chdiv">低层</span>
                        <span class="chdiv mal10">多层</span>
                        <span class="chdiv mal10">小高层</span>
                        <span class="chdiv mal10">高层</span>
                        <span class="chdiv mal10">超高层</span>
                        <em>可单选，也可复选</em>
                    </dd>
                </dl>
                <dl>
                    <dt><i></i>物业类型</dt>
                    <dd id="ls_pop_operastion">
                        <span data-type="R" class="chdiv">住宅</span>
                        <span data-type="V" class="chdiv mal10">别墅</span>
                        <span data-type="O" class="chdiv mal10">写字楼</span>
                        <span data-type="S" class="chdiv mal10">商铺</span>
                        <em>可单选，也可复选</em>
                    </dd>
                </dl>
                <dl>
                    <dt><i></i>上传图片</dt>
                    <dd>
                        <em>限8张</em>
                        <div class="chpic">
                            <ul id="ls_pop_picBox">
                                <li id="ls_pop_addPicPos">
                                </li>
                            </ul>
                        </div>
                    </dd>
                    <a id="ls_pop_showLess" class="brn_stop" href="javascript:void(0);">收起信息<img
                            src="//img1.soufunimg.com/house/images/search/btn02.png" width="11" height="6"/></a>
                </dl>
            </div>
            <a id="ls_pop_submit" class="btn" href="javascript:void(0);">提交</a>
            <div id="ls_pop_map" style="display:none;z-index: 1000 !important;" class="mapdiv">

            </div>
        </div>
    </div>
    </div>
</div>

<div id="ls_success" class="formwrapopen" style="display: none;z-index: 10001 !important;">
    <div class="examine">
        <!--<a class="close" href="#"></a>-->
        <p>感谢您提交新楼盘！<br />
            我们会尽快审核</p></div>
</div>
<script>
{
    pageConfig.adddianpingConfig = {
        imageuploadurl: '//wuhan.newhouse.fang.com/loupan/2610156494/house/ajax/dianping/imageupload',
        adddianpingurl: '//wuhan.newhouse.fang.com/loupan/2610156494/house/ajax/dianping/adddianping',
    }
}
</script>
<style>  
    #filePicker div:nth-child(2){width:100%!important;height:100%!important;}  
</style>  


</div>

    
    <div class="disclaimer" style="width: 1160px;line-height: 20px;margin: 10px auto 8px auto;padding: 15px 20px;background: #eee;"><strong>免责声明</strong>：本站楼盘信息旨在为用户提供更多信息的无偿服务，信息以政府部门登记备案为准，请谨慎核查。</div>
<link href="//static.soufunimg.com/newhouse/style/newhouse_footer.css?v=20160318" type="text/css" rel="stylesheet" />
<!--20120411房天下统一版尾begin-->
<div class="sfunfooter20120411">
    <div class="verdana">
        <a href="http://www.fang.com/aboutus/index.asp" target="_blank">关于我们</a>‖
        <a href="http://www.fang.com/hezuo_file/house/index.html" target="_blank">网站合作</a>‖
        <a href="http://www.fang.com/aboutus/contactus.html" target="_blank">联系我们</a>‖
        <a href="http://job.fang.com/index.html" target="_blank">招聘信息</a>‖
        <span onmouseover="this.className='footershaixa activexiala'" onmouseout="this.className='footershaixa'" style="width:80px" class="footershaixa"><a href="http://www.fang.com/SoufunFamily.htm">房天下家族</a>‖<div class="footershaixb">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td width="16"><b style="color:#c00;">B</b></td>
                    <td width="80"><a href="http://bj.fang.com/" target="_blank">北京房地产</a></td>
                    <td width="16"><b style="color:#c00;">D</b></td>
                    <td width="80"><a href="http://dg.fang.com/" target="_blank">东莞房地产</a></td>
                    <td width="16">&nbsp;</td>
                    <td width="80"><a href="http://hn.fang.com/" target="_blank">海南房地产</a></td>
                    <td width="16">&nbsp;</td>
                    <td width="100"><a href="http://nn.fang.com/" target="_blank">南宁房地产</a></td>
                    <td width="16">&nbsp;</td>
                    <td width="80"><a href="http://sy.fang.com/" target="_blank">沈阳房地产</a></td>
                </tr>
                <tr>
                    <td><b style="color:#c00;">C</b></td>
                    <td><a href="http://cd.fang.com/" target="_blank">成都房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://dl.fang.com/" target="_blank">大连房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://hf.fang.com" target="_blank">合肥房地产</a></td>
                    <td><b style="color:#c00;">Q</b></td>
                    <td><a href="http://qd.fang.com/" target="_blank">青岛房地产</a></td>
                    <td><b style="color:#c00;">T</b></td>
                    <td><a href="http://tj.fang.com/" target="_blank">天津房地产</a></td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><a href="http://cq.fang.com/" target="_blank">重庆房地产</a></td>
                    <td><b style="color:#c00;">F</b></td>
                    <td><a href="http://fz.fang.com/" target="_blank">福州房地产</a></td>
                    <td><b style="color:#c00;">J</b></td>
                    <td><a href="http://jn.fang.com/" target="_blank">济南房地产</a></td>
                    <td><b style="color:#c00;">S</b></td>
                    <td><a href="http://sh.fang.com/" target="_blank">上海房地产</a></td>
                    <td><b style="color:#c00;">W</b></td>
                    <td><a href="http://wuhan.fang.com/" target="_blank">武汉房地产</a></td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><a href="http://cs.fang.com/" target="_blank">长沙房地产</a></td>
                    <td><b style="color:#c00;">G</b></td>
                    <td><a href="http://gz.fang.com/" target="_blank">广州房地产</a></td>
                    <td><b style="color:#c00;">N</b></td>
                    <td><a href="http://nanjing.fang.com/" target="_blank">南京房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://sz.fang.com/" target="_blank">深圳房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://wuxi.fang.com/" target="_blank">无锡房地产</a></td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><a href="http://changchun.fang.com/" target="_blank">长春房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://gy.fang.com" target="_blank">贵阳房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://nc.fang.com/" target="_blank">南昌房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://suzhou.fang.com/" target="_blank">苏州房地产</a></td>
                    <td><b style="color:#c00;">X</b></td>
                    <td><a href="http://xian.fang.com/" target="_blank">西安房地产</a></td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><a href="http://cz.fang.com/" target="_blank">常州房地产</a></td>
                    <td><b style="color:#c00;">H</b></td>
                    <td><a href="http://hz.fang.com/" target="_blank">杭州房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://nb.fang.com/" target="_blank">宁波房地产</a></td>
                    <td>&nbsp;</td>
                    <td><a href="http://sjz.fang.com/" target="_blank">石家庄房地产</a></td>

                    <td><b style="color:#c00;">Z</b></td>
                    <td><a href="http://zz.fang.com/" target="_blank">郑州房地产</a></td>
                </tr>

                </tbody></table>
            <div style="text-align:right;padding:0px;"><a href="http://www.fang.com/SoufunFamily.htm" target="_blank">进入房天下家族&gt;&gt;</a></div>
        </div></span>
        <a href="http://www.fang.com/sitemap.html" target="_blank">网站地图</a>‖
        <a href="https://chatclient.3g.fang.com/webim/ocssim.htm" target="_blank">意见反馈</a>‖
        <a href="http://wap.fang.com/xc/mobile.html" target="_blank">手机房天下</a>‖
        <a href="http://open.fang.com" target="_blank">开放平台</a>‖
        <a href="http://www.fang.com/aboutus/copyright.html" target="_blank">服务声明</a>‖
        <a href="https://news.fang.com/zt/201805/xinbaichengzhanlue123.html " target="_blank">加盟房天下</a>
    </div>

    <div class="verdana">Copyright &copy; <script language="javascript">
        var dt = new Date();
        y = dt.getFullYear(); //获取年(四位)
        document.write(y)</script> 北京搜房科技发展有限公司</div>
    <div class="song" style="line-height:23px;position:relative;z-index:1;font-family:Verdana;">Beijing SouFun Science&Technology Development Co.,Ltd 版权所有</div>
    <div class="song">违法和不良信息举报电话：010-56318764 举报邮箱：<a href="mailto:jubao@fang.com" rel="nofollow"><em>jubao@fang.com</em></a></div>

</div>
<script type="text/javascript" src="//img.soufunimg.com/newhousedata/images/support/FQA.js"></script>


<script type="text/javascript" src="//img.soufunimg.com/newhousedata/images/support/FQA.js"></script>





    
         <link href="//static.soufunimg.com/esf/esf/online/loupannew/static/css/housevilla/common/rightTools.css?v=202109160001" rel="stylesheet"/>
<!-- 大首页右侧边栏 start -->
<div class="rsideV02" id="hideTabdiv">
<div class="barbox">
	 <ul>
        <li>
        	<a class="no2" href="https://my.fang.com/MyCollect/Index.html?city=wuhan" target="_blank">
            	<span>收藏</span>
                <div class="sideboxleft"><div class="txtinfo">我的收藏</div></div>
            </a>
        </li>
        <li>
        	<a class="no3" href="https://newhouse.fang.com/house/tools.htm" target="_blank">
            	<span>贷款计算器</span>
                <div class="sideboxleft"><div class="txtinfo">贷款计算器</div></div>
            </a>
        </li>
        <li class="w166">
        	<a class="no5" style="cursor:pointer;">
            	<span>下载</span>
                <div class="sideboxleft">
                	<div class="txtinfo">
                      <div class="qrcodepic"><img src="//static.soufunimg.com/homepage/new/fang905bj/newsV3/images/qrc01new.png" alt="" /></div>
                      <p>下载房天下APP<br />0元抢拍特价房</p>
                    </div>
          		</div>
            </a>
        </li>
        <li class="w166">
        	<a class="no6" style="cursor:pointer;">
            	<span>公众号</span>
            	<div class="sideboxleft">
                	<div class="txtinfo">
                      <div class="qrcodepic"><img src="//static.soufunimg.com/homepage/new/fang905bj/newsV3/images/qrc02.jpg" alt="" /></div>
                      <p>关注房天下公众号<br/>特价房早知道</p>
          			</div>
                </div>
            </a>
        </li>
        <li>
        	<a class="no7" id="rightToolsFeedback" style="cursor:pointer;">
            	<span>在线客服</span>
                <div class="sideboxleft"><div class="txtinfo">在线客服</div></div>
            </a>
        </li>
        <li id="backTop" style="display:none;">
        	<a class="no8" id="topScroll" style="cursor:pointer;">
            	<span></span>
                <div class="sideboxleft"><div class="txtinfo">返回顶部</div></div>
            </a>
        </li>
     </ul>
</div>
</div>
<!-- 大首页右侧边栏 end -->

     
    
    
	
	<script>
    pageConfig.publicConfig = {
        // 城市名
        city: '武汉',
        // m站城市缩写
        m_city: 'wuhan',
        // 楼盘ID
        newcode: '2610156494',
        // 楼盘名
        projname: '华侨城·欢乐天际',
        // 物业类型
        purpose: '住宅',
        // 物业类型 R ,O,S,V
        operastion: 'R',
        // 区县
        district: '青山',
        // 商圈
        comarea: '工业四路',
        domain: 'huanletianjihqc.fang.com/',
        // 南北方
        region: 'south',
        // 环境 'Y'：正式环境
        online: 'Y',
        //新房城市域名
        newhouseDomain:'//wuhan.newhouse.fang.com',
        // 小区网城市域名
        esfDomain:'//wuhan.esf.fang.com',
        //地址
        address:'团结大道地铁4号线工业四路站B出口',
        //图片
        pic:'//imgwcs2.soufunimg.com/house/2020_08/21/513a7276-3466-4a8f-bb05-8a7b244da875.jpg',
        //价格
        price:'21000元/平方米',
        urlPath:'//wuhan.newhouse.fang.com/loupan/2610156494',
    }
</script>
    <script>
    // 搜索配置
    pageConfig.pageConfig = {
        pageid: 'xf_lp^xq_pc',
        pageType:'xiangqing',
    };
    pageConfig.entranceType = 'second_detail',
   	pageConfig.pageid = 'xf_lp^xq_pc',
    // 收藏配制
    pageConfig.collectionProjectConfig = {
        url: '/loupan/shop/2610156494/ajax/collectproject',
        requestPage: 'new',
    };
    pageConfig.activeConfig = {
        stpage: 'xf_lp^xq_pc',
    };
    </script>
	<script>
        fang('housevilla/main_housevilla_xfxiangqing');
	</script>

    
    
    

    <script>
        (function () {
            var bp = document.createElement('script');
            var curProtocol = window
                .location
                .protocol
                .split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'http://push.zhanzhang.baidu.com/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s
                .parentNode
                .insertBefore(bp, s);
        })();
    </script>

    
</body>
</html>
'''
body = '<ul class="list clearfix"><li><div class="list-left">物业类别：</div><div class="list-right" title="普通住宅,商住公寓,LOFT">普通住宅,商住公寓,LOFT</div></li></ul>'

# content = '''
# <ul class="list clearfix">
#                         <li>
#                             <div class="list-left">物业类别：</div>
#                             <div class="list-right" title="普通住宅,商住公寓,LOFT">普通住宅,商住公寓,LOFT</div>
#                         </li>
#                         <li>
#                         <div class="list-left">项目特色：</div>
#                         <div class="list-right" style="height:32px;">
#
#
#                                     <span class="tag">品牌地产</span>
#
#                                     <span class="tag">地铁沿线</span>
#
#
#                         </li>
#                         <li>
#                             <div class="list-left">建筑类别：</div>
#                             <div class="list-right">
#                                 <span class="bulid-type">板楼</span>
#                             </div>
#                         </li>
#                         <li>
#                             <div class="list-left">装修状况：</div>
#                             <div class="list-right">
#
#                                     毛坯
#
#                             </div>
#                         </li>
#                         <li>
#                             <div class="list-left">产权年限：</div>
#                             <div class='list-right'>
#                                 <div class='clearfix cqnx_512'>
#
#
#                                         <p style="width: 150px;float: left;">普通住宅:70年</p>
#
#                                         <p style="width: 150px;float: left;">商住公寓:40年</p>
#
#                                         <p style="width: 150px;float: left;">LOFT:40年</p>
#
#
#                                 </div>
#                             </div>
#                         </li>
#
#                         <li>
#                             <div class="list-left">环线位置：</div>
#                             <div class="list-right">二至三环</div>
#                         </li>
#
#                         <li class="list-text">
#                             <div class="list-left">开<i style="margin-right: 6px;"></i>发<i style="margin-right: 6px;"></i> 商：</div>
#                             <div class="list-right-text"><a href="https://baike.fang.com/item/武汉华侨城实业发展有限公司/1216199" target="_blank">武汉华侨城实业发展有限公司</a></div>
#                         </li>
#                         <li class="list-text">
#                             <div class="list-left">楼盘地址：</div>
#                             <div class="list-right-text">团结大道地铁4号线工业四路站B出口</div>
#                         </li>
#                     </ul>
#                 </div>'''

aaa = Selector(text=content).xpath('//div[contains(.,"基本信息")]/parent/text()').getall()
aa = Selector(text=content).xpath('(//ul[@class="clearfix list"])/li[11]/div[2]/text()').get()
a = Selector(text=content).css('div.main-item ul.list.clearfix li:nth-child(6) div:nth-child(2)::text').get().strip()
next_url = Selector(text=content).xpath('//a[@class="next"]/@href').get()
print(next_url)