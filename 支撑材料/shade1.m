clc;
clear;
%αs表示太阳高度角,γs表示太阳方位角%
ARFAs=61.75778607/180*pi;
% GAMAs=134.7568993/180*pi;

d=13;
w=6;
% 
% %R为定日镜位置，A为吸收塔位置%
% h=80;
% 
% xR=337.032;
% yR=-8.210;
% 
% xRA=-xR/(sqrt(xR*xR+yR*yR+h*h));
% yRA=-yR/(sqrt(xR*xR+yR*yR+h*h));
% zRA=h/(sqrt(xR*xR+yR*yR+h*h));
% 
% 
% %RS与RA的夹角为β%
% % cos(BETA)=-cos(ARFAs)*cos(GAMAs)*xRA+cos(ARFAs)*sin(GAMAs)*yRA+sin(ARFAs)*zRA;
% BETA=acos(-cos(ARFAs)*cos(GAMAs)*xRA+cos(ARFAs)*sin(GAMAs)*yRA+sin(ARFAs)*zRA);
% % BETA=BETA/pi*180;
% 
% %镜面法向量的高度角和方位角%
% % sin(ARFAn)=(zRA+sin(ARFAs))/(2*cos(BETA/2));
% % tan(GAMAn)=-(yRA+cos(ARFAs)*sin(GAMAs))/(xRA-cos(ARFAs)*cos(GAMAs));
% ARFAn=asin((zRA+sin(ARFAs))/(2*cos(BETA/2)));
% GAMAn=atan(-(yRA+cos(ARFAs)*sin(GAMAs))/(xRA-cos(ARFAs)*cos(GAMAs)));
% % ARFAn=ARFAn/pi*180;
% % GAMAn=GAMAn/pi*180;

ARFAh=/180*pi;
% 90.9350192	74.50021526	91.71090324	91.11532062	82.24182924	68.85907559	78.22850598	37.31712927	91.25199395	28.29002814	48.65826636	115.4801436
% -0.9350192	15.49978474	-1.710903238	-1.115320622	7.758170764	21.14092441	11.77149402	52.68287073	-1.251993954	61.70997186	41.34173364	-25.48014361

ita=(d*tan(ARFAs))/(w*cos(ARFAh)*(tan(ARFAs)+tan(ARFAh)));

disp(ita);



