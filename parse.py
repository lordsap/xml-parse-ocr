import xml.etree.ElementTree as ET

ns = {'html': "http://www.w3.org/1999/xhtml"}

text2 = "<html:html xmlns:html=\"http://www.w3.org/1999/xhtml\" lang=\"en\" xml:lang=\"en\">\n <html:head>\n  <html:title />\n<html:meta content=\"text/html;charset=utf-8\" http-equiv=\"Content-Type\" />\n  <html:meta content=\"tesseract 4.0.0-beta.4-50-g07acc\" name=\"ocr-system\" />\n  <html:meta content=\"ocr_page ocr_carea ocr_par ocr_line ocrx_word\" name=\"ocr-capabilities\" />\n</html:head>\n<html:body>\n  <html:div class=\"ocr_page\" id=\"page_1\" rotation=\"270\" title=\"image &quot;/home/vcap/tmp/b91d9d27-911c-4115-99c3-816ba407606e0/l312.pdf1.png&quot;; bbox 0 0 2550 3300; ppageno 0\">\n   <html:div class=\"ocr_carea\" id=\"block_1_1\" title=\"bbox 654 2534 683 3208\">\n    <html:p class=\"ocr_par\" id=\"par_1_1\" lang=\"eng\" title=\"bbox 654 2534 683 3208\">\n     <html:span class=\"ocr_line\" id=\"line_1_1\" title=\"bbox 654 2534 683 3208; textangle 90; x_size 29; x_descenders 6; x_ascenders 8\">\n      <html:span class=\"ocrx_word\" id=\"word_1_1\" title=\"bbox 657 3072 683 3208; x_wconf 79\">Summary</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_2\" title=\"bbox 657 2953 683 3049; x_wconf 80\">Recap</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_3\" title=\"bbox 656 2893 677 2929; x_wconf 84\">of</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_4\" title=\"bbox 656 2753 683 2869; x_wconf 79\">Budget</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_5\" title=\"bbox 654 2534 678 2731; x_wconf 70\">Activities</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_2\" title=\"bbox 768 2593 1023 3211\">\n    <html:p class=\"ocr_par\" id=\"par_1_2\" lang=\"eng\" title=\"bbox 768 2934 791 3208\">\n     <html:span class=\"ocr_line\" id=\"line_1_2\" title=\"bbox 768 2934 791 3208; textangle 90; x_size 29.16013; x_descenders 6.1601305; x_ascenders 8\">\n      <html:span class=\"ocrx_word\" id=\"word_1_6\" title=\"bbox 768 3112 791 3208; x_wconf 78\">Basic</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_7\" title=\"bbox 770 2934 791 3090; x_wconf 80\">Research</html:span>\n     </html:span>\n    </html:p>\n\n    <html:p class=\"ocr_par\" id=\"par_1_3\" lang=\"eng\" title=\"bbox 843 2893 872 3211\">\n     <html:span class=\"ocr_line\" id=\"line_1_3\" title=\"bbox 843 2893 872 3211; textangle 90; x_size 29; x_descenders 6; x_ascenders 8\">\n      <html:span class=\"ocrx_word\" id=\"word_1_8\" title=\"bbox 843 3072 872 3211; x_wconf 71\">Applied</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_9\" title=\"bbox 845 2893 866 3049; x_wconf 82\">Research</html:span>\n     </html:span>\n    </html:p>\n\n    <html:p class=\"ocr_par\" id=\"par_1_4\" lang=\"eng\" title=\"bbox 920 2593 1023 3211\">\n     <html:span class=\"ocr_line\" id=\"line_1_4\" title=\"bbox 920 2593 948 3211; textangle 90; x_size 28; x_descenders 6; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_10\" title=\"bbox 920 3052 942 3211; x_wconf 73\">Advanced</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_11\" title=\"bbox 920 2833 948 3030; x_wconf 72\">Technology</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_12\" title=\"bbox 920 2593 948 2809; x_wconf 74\">Development</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_5\" title=\"bbox 996 2854 1023 3211; textangle 90; x_size 25; x_descenders 6; x_ascenders 4\">\n      <html:span class=\"ocrx_word\" id=\"word_1_13\" title=\"bbox 998 3013 1023 3211; x_wconf 79\">Management</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_14\" title=\"bbox 996 2854 1023 2989; x_wconf 78\">Support</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_3\" title=\"bbox 1071 2193 1100 3109\">\n    <html:p class=\"ocr_par\" id=\"par_1_5\" lang=\"eng\" title=\"bbox 1071 2193 1100 3109\">\n     <html:span class=\"ocr_line\" id=\"line_1_6\" title=\"bbox 1071 2193 1100 3109; textangle 90; x_size 31; x_descenders 8; x_ascenders 8\">\n      <html:span class=\"ocrx_word\" id=\"word_1_15\" title=\"bbox 1071 3015 1092 3109; x_wconf 86\">Total</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_16\" title=\"bbox 1071 2821 1097 2991; x_wconf 78\">Research,</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_17\" title=\"bbox 1071 2560 1100 2790; x_wconf 78\">Development,</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_18\" title=\"bbox 1073 2455 1094 2530; x_wconf 80\">Test</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_19\" title=\"bbox 1076 2416 1094 2428; x_wconf 66\"><html:strong>6</html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_20\" title=\"bbox 1071 2193 1095 2391; x_wconf 68\">Evaluation</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_4\" title=\"bbox 1185 2614 1212 3208\">\n    <html:p class=\"ocr_par\" id=\"par_1_6\" lang=\"eng\" title=\"bbox 1185 2614 1212 3208\">\n     <html:span class=\"ocr_line\" id=\"line_1_7\" title=\"bbox 1185 2614 1212 3208; textangle 90; x_size 27; x_descenders 6; x_ascenders 5\">\n      <html:span class=\"ocrx_word\" id=\"word_1_21\" title=\"bbox 1187 3072 1212 3208; x_wconf 82\">Summary</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_22\" title=\"bbox 1187 2953 1212 3051; x_wconf 82\">Recap</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_23\" title=\"bbox 1185 2893 1206 2931; x_wconf 86\">of</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_24\" title=\"bbox 1187 2794 1209 2869; x_wconf 73\">FYDP</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_25\" title=\"bbox 1187 2614 1212 2769; x_wconf 82\">Programs</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_5\" title=\"bbox 1298 2734 1325 3210\">\n    <html:p class=\"ocr_par\" id=\"par_1_7\" lang=\"eng\" title=\"bbox 1298 2734 1325 3210\">\n     <html:span class=\"ocr_line\" id=\"line_1_8\" title=\"bbox 1298 2734 1325 3210; textangle 90; x_size 27; x_descenders 6; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_26\" title=\"bbox 1298 3052 1319 3210; x_wconf 83\">Research</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_27\" title=\"bbox 1298 2973 1319 3030; x_wconf 83\">and</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_28\" title=\"bbox 1298 2734 1325 2950; x_wconf 81\">Development</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_6\" title=\"bbox 1373 2194 1401 3111\">\n    <html:p class=\"ocr_par\" id=\"par_1_8\" lang=\"eng\" title=\"bbox 1373 2194 1401 3111\">\n     <html:span class=\"ocr_line\" id=\"line_1_9\" title=\"bbox 1373 2194 1401 3111; textangle 90; x_size 27; x_descenders 6; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_29\" title=\"bbox 1373 3015 1395 3111; x_wconf 76\">Total</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_30\" title=\"bbox 1373 2821 1398 2991; x_wconf 79\">Research,</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_31\" title=\"bbox 1373 2562 1401 2790; x_wconf 75\">Development,</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_32\" title=\"bbox 1374 2455 1395 2530; x_wconf 82\">Test</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_33\" title=\"bbox 1377 2416 1395 2430; x_wconf 78\">&amp;</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_34\" title=\"bbox 1373 2194 1396 2391; x_wconf 80\">Evaluation</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_7\" title=\"bbox 130 1275 309 2030\">\n    <html:p class=\"ocr_par\" id=\"par_1_9\" lang=\"eng\" title=\"bbox 130 1275 309 2030\">\n     <html:span class=\"ocr_line\" id=\"line_1_10\" title=\"bbox 130 1533 151 1770; textangle 90; x_size 29.519482; x_descenders 6.7142859; x_ascenders 6.090909\">\n      <html:span class=\"ocrx_word\" id=\"word_1_35\" title=\"bbox 130 1533 151 1770; x_wconf 74\">UNCLASSIFIED</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_11\" title=\"bbox 205 1454 232 1869; textangle 90; x_size 27; x_descenders 6; x_ascenders 5\">\n      <html:span class=\"ocrx_word\" id=\"word_1_36\" title=\"bbox 205 1674 232 1869; x_wconf 77\">Department</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_37\" title=\"bbox 205 1614 226 1649; x_wconf 82\">of</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_38\" title=\"bbox 205 1454 226 1589; x_wconf 86\">Defense</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_12\" title=\"bbox 243 1395 271 1910; textangle 90; x_size 28; x_descenders 6; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_39\" title=\"bbox 244 1874 264 1910; x_wconf 87\">FY</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_40\" title=\"bbox 243 1775 264 1850; x_wconf 83\">2019</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_41\" title=\"bbox 243 1535 265 1749; x_wconf 75\">President's</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_42\" title=\"bbox 243 1395 271 1511; x_wconf 83\">Budget</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_13\" title=\"bbox 279 1275 309 2030; textangle 90; x_size 30; x_descenders 7; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_43\" title=\"bbox 279 1895 301 2030; x_wconf 84\">Exhibit</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_44\" title=\"bbox 280 1815 301 1871; x_wconf 40\">R41</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_45\" title=\"bbox 282 1754 301 1790; x_wconf 86\">FY</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_46\" title=\"bbox 280 1655 301 1730; x_wconf 83\">2019</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_47\" title=\"bbox 280 1415 303 1629; x_wconf 82\">President's</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_48\" title=\"bbox 280 1275 309 1391; x_wconf 78\">Budget</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_8\" title=\"bbox 318 1373 381 1931\">\n    <html:p class=\"ocr_par\" id=\"par_1_10\" lang=\"eng\" title=\"bbox 318 1373 381 1931\">\n     <html:span class=\"ocr_line\" id=\"line_1_14\" title=\"bbox 318 1373 346 1931; textangle 90; x_size 28; x_descenders 6; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_49\" title=\"bbox 318 1835 340 1931; x_wconf 86\">Total</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_50\" title=\"bbox 318 1574 346 1811; x_wconf 78\">Obligational</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_51\" title=\"bbox 318 1373 346 1551; x_wconf 68\">Authority</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_15\" title=\"bbox 355 1442 381 1863; textangle 90; x_size 28; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_52\" title=\"bbox 355 1715 381 1863; x_wconf 80\">(Dollars</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_53\" title=\"bbox 355 1653 378 1689; x_wconf 73\">in</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_54\" title=\"bbox 357 1442 381 1631; x_wconf 77\">Thousands)</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_9\" title=\"bbox 619 1337 679 2031\">\n    <html:p class=\"ocr_par\" id=\"par_1_11\" lang=\"eng\" title=\"bbox 619 1337 679 2031\">\n     <html:span class=\"ocr_line\" id=\"line_1_16\" title=\"bbox 619 1337 642 2031; textangle 90; x_size 27.5; x_descenders 5.5; x_ascenders 5.5\">\n      <html:span class=\"ocrx_word\" id=\"word_1_55\" title=\"bbox 622 1994 642 2031; x_wconf 81\">FY</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_56\" title=\"bbox 619 1896 642 1971; x_wconf 77\">2019</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_57\" title=\"bbox 622 1713 642 1752; x_wconf 81\">FY</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_58\" title=\"bbox 621 1616 642 1690; x_wconf 83\">2019</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_59\" title=\"bbox 622 1434 642 1471; x_wconf 85\">FY</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_60\" title=\"bbox 621 1337 642 1411; x_wconf 85\">2019</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_17\" title=\"bbox 658 1357 679 1992; textangle 90; x_size 26.333334; x_descenders 5.3333335; x_ascenders 5\">\n      <html:span class=\"ocrx_word\" id=\"word_1_61\" title=\"bbox 660 1916 679 1992; x_wconf 78\">Base</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_62\" title=\"bbox 660 1654 679 1711; x_wconf 86\">OCO</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_63\" title=\"bbox 658 1357 679 1452; x_wconf 83\">Total</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_10\" title=\"bbox 771 1299 1024 2031\">\n    <html:p class=\"ocr_par\" id=\"par_1_12\" lang=\"eng\" title=\"bbox 771 1299 949 2031\">\n     <html:span class=\"ocr_line\" id=\"line_1_18\" title=\"bbox 771 1299 798 1990; textangle 90; x_size 38.75; x_descenders 6.5; x_ascenders 10.75\">\n      <html:span class=\"ocrx_word\" id=\"word_1_64\" title=\"bbox 771 1857 798 1990; x_wconf 83\">469,955</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_65\" title=\"bbox 771 1299 798 1431; x_wconf 84\">469,955</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_19\" title=\"bbox 846 1299 874 2029; textangle 90; x_size 38.75; x_descenders 6.5; x_ascenders 10.75\">\n      <html:span class=\"ocrx_word\" id=\"word_1_66\" title=\"bbox 846 1858 873 2029; x_wconf 81\">1,431,468</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_67\" title=\"bbox 847 1299 874 1470; x_wconf 78\">1,431,469</html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_20\" title=\"bbox 922 1300 949 2031; textangle 90; x_size 38.75; x_descenders 6.5; x_ascenders 10.75\">\n      <html:span class=\"ocrx_word\" id=\"word_1_68\" title=\"bbox 922 1858 948 2031; x_wconf 81\">1,458,054</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_69\" title=\"bbox 922 1300 949 1471; x_wconf 78\">1,458,054</html:span>\n     </html:span>\n    </html:p>\n\n    <html:p class=\"ocr_par\" id=\"par_1_13\" lang=\"eng\" title=\"bbox 997 1299 1024 1972\">\n     <html:span class=\"ocr_line\" id=\"line_1_21\" title=\"bbox 997 1299 1024 1972; textangle 90; x_size 38.75; x_descenders 6.5; x_ascenders 10.75\">\n      <html:span class=\"ocrx_word\" id=\"word_1_70\" title=\"bbox 997 1857 1024 1972; x_wconf 82\">79,289</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_71\" title=\"bbox 997 1299 1024 1411; x_wconf 82\">79,289</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_11\" title=\"bbox 1072 1299 1099 2031\">\n    <html:p class=\"ocr_par\" id=\"par_1_14\" lang=\"eng\" title=\"bbox 1072 1299 1099 2031\">\n     <html:span class=\"ocr_line\" id=\"line_1_22\" title=\"bbox 1072 1299 1099 2031; textangle 90; x_size 29.037037; x_descenders 7.2592592; x_ascenders 7.2592592\">\n      <html:span class=\"ocrx_word\" id=\"word_1_72\" title=\"bbox 1072 1857 1099 2031; x_wconf 79\">3,438,766</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_73\" title=\"bbox 1074 1299 1099 1471; x_wconf 75\">3,438,766</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_12\" title=\"bbox 1299 1299 1326 2031\">\n    <html:p class=\"ocr_par\" id=\"par_1_15\" lang=\"eng\" title=\"bbox 1299 1299 1326 2031\">\n     <html:span class=\"ocr_line\" id=\"line_1_23\" title=\"bbox 1299 1299 1326 2031; textangle 90; x_size 29.5; x_descenders 7.375; x_ascenders 7.375\">\n      <html:span class=\"ocrx_word\" id=\"word_1_74\" title=\"bbox 1299 1857 1326 2031; x_wconf 73\">3,438,766</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_75\" title=\"bbox 1299 1299 1326 1471; x_wconf 76\">3,438,766</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_13\" title=\"bbox 1374 1299 1401 2031\">\n    <html:p class=\"ocr_par\" id=\"par_1_16\" lang=\"eng\" title=\"bbox 1374 1299 1401 2031\">\n     <html:span class=\"ocr_line\" id=\"line_1_24\" title=\"bbox 1374 1299 1401 2031; textangle 90; x_size 37.75; x_descenders 5.5; x_ascenders 10.75\">\n      <html:span class=\"ocrx_word\" id=\"word_1_76\" title=\"bbox 1374 1857 1401 2031; x_wconf 77\">3,438,766</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_77\" title=\"bbox 1375 1299 1401 1473; x_wconf 76\">3,438,766</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_14\" title=\"bbox 2316 1402 2347 3211\">\n    <html:p class=\"ocr_par\" id=\"par_1_17\" lang=\"eng\" title=\"bbox 2316 1402 2347 3211\">\n     <html:span class=\"ocr_line\" id=\"line_1_25\" title=\"bbox 2316 1402 2347 3211; textangle 90; x_size 27; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_78\" title=\"bbox 2319 3059 2340 3211; x_wconf 32\">R4119PB:</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_79\" title=\"bbox 2321 2995 2340 3031; x_wconf 86\">FY</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_80\" title=\"bbox 2318 2897 2340 2971; x_wconf 82\">2019</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_81\" title=\"bbox 2316 2657 2340 2870; x_wconf 79\">President's</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_82\" title=\"bbox 2319 2516 2346 2632; x_wconf 81\">Budget</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_83\" title=\"bbox 2318 2296 2343 2486; x_wconf 81\">(Published</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_84\" title=\"bbox 2319 2104 2346 2275; x_wconf 78\">Version),</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_85\" title=\"bbox 2326 2039 2341 2074; x_wconf 88\">as</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_86\" title=\"bbox 2320 1979 2341 2014; x_wconf 88\">of</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_87\" title=\"bbox 2322 1817 2347 1955; x_wconf 75\">January</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_88\" title=\"bbox 2320 1747 2346 1795; x_wconf 82\">26,</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_89\" title=\"bbox 2320 1642 2341 1715; x_wconf 80\">2018</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_90\" title=\"bbox 2322 1579 2341 1615; x_wconf 90\">at</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_91\" title=\"bbox 2320 1402 2341 1553; x_wconf 72\">12:42:28</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_15\" title=\"bbox 2436 1538 2455 1775\">\n    <html:p class=\"ocr_par\" id=\"par_1_18\" lang=\"eng\" title=\"bbox 2436 1538 2455 1775\">\n     <html:span class=\"ocr_line\" id=\"line_1_26\" title=\"bbox 2436 1538 2455 1775; textangle 90; x_size 26; x_descenders 6.5; x_ascenders 6.5\">\n      <html:span class=\"ocrx_word\" id=\"word_1_92\" title=\"bbox 2436 1538 2455 1775; x_wconf 70\">UNCLASSIFIED</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_16\" title=\"bbox 322 177 344 392\">\n    <html:p class=\"ocr_par\" id=\"par_1_19\" lang=\"eng\" title=\"bbox 322 177 344 392\">\n     <html:span class=\"ocr_line\" id=\"line_1_27\" title=\"bbox 322 177 344 392; textangle 90; x_size 29.666666; x_descenders 7.4166665; x_ascenders 7.4166665\">\n      <html:span class=\"ocrx_word\" id=\"word_1_93\" title=\"bbox 322 356 344 392; x_wconf 87\">26</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_94\" title=\"bbox 323 275 344 330; x_wconf 79\">Jan</html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_95\" title=\"bbox 322 177 344 251; x_wconf 84\">2018</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_17\" title=\"bbox 2387 78 2436 490\">\n    <html:p class=\"ocr_par\" id=\"par_1_20\" lang=\"eng\" title=\"bbox 2387 78 2436 490\">\n     <html:span class=\"ocr_line\" id=\"line_1_28\" title=\"bbox 2387 78 2436 490; textangle 90; x_size 66; x_descenders 16.5; x_ascenders 16.5\">\n      <html:span class=\"ocrx_word\" id=\"word_1_96\" title=\"bbox 2387 78 2436 490; x_wconf 60\">m</html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n  </html:div>\n </html:body>\n</html:html>"
text2 = text2.strip('\n')

tree = ET.fromstring(text2)
# print(tree)
all_elements = tree.findall('html:body', ns)
print(len(all_elements))
all_elements = tree.findall('.//{http://www.w3.org/1999/xhtml}span/', ns)
print(len(all_elements))

try:
    open('export_text.txt','w').close()
except:
    print('Not made yet')
f = open('export_text.txt','w')

for node in tree.iter():
    word = False
    line = False
    if('class' in node.attrib):
        if(node.attrib['class'] == 'ocr_line'):
            line = True
        if(node.attrib['class'] == 'ocrx_word'):
            word = True
        if(line):
            print('---------------NEW LINE----------------------------------------------------------------')
            f.write('---------------NEW LINE----------------------------------------------------------------' + '\n')
        if(line or word):
            print('node: \t\t\t' + str(node))
            f.write('node: \t\t\t\t' + str(node) + '\n')
            print('attrib: \t\t' + str(node.attrib))
            f.write('attrib: \t\t\t' + str(node.attrib) + '\n')
            print('attrib[\'class\']: \t' + str(node.attrib['class']))
            f.write('attrib[\'class\']: \t' + str(node.attrib['class']) + '\n')
            print('attrib[\'title\']: \t' + str(node.attrib['title']))
            f.write('attrib[\'title\']: \t' + str(node.attrib['title']) + '\n')
        if(word):
            print('text: \t\t\t' + str(node.text))
            f.write('text: \t\t\t\t' + str(node.text) + '\n')
        print()
        f.write('\n')

# for node in all_elements:
#     print('node: \t\t\t' + str(node))
#     print('attrib: \t\t' + str(node.attrib))
#     print('attrib[\'class\']: \t' + str(node.attrib['class']))
#     print('attrib[\'title\']: \t' + str(node.attrib['title']))
#     print('text: \t\t\t' + node.text)
#     print()