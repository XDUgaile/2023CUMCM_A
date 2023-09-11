%α表示太阳高度角,A表示太阳方位角%
A=134.7568993;
ARFA=-5.26311562;


%入射光线的方向余弦%
cosARFAi=cos(A)*cos(ARFA);
cosBETAi=sin(A)*cos(ARFA);
cosGAMAi=sin(ARFA);

%EH,AH分别表示定日镜跟踪太阳时的俯仰角和方位角%
%近似处理成太阳高度角和方位角%
EH=ARFA;
AH=A;

%XgH,YgH,ZgH表示定日镜的镜面中心在地面坐标系中的坐标%
XgH=107.250;
YgH=11.664;
ZgH=4;


%由镜面坐标系向地面坐标系的变换矩阵%
M1=[-sin(AH) -cos(AH)*cos(EH) cos(AH)*sin(EH) XgH;
    cos(AH) -sin(AH)*cos(EH) sin(AH)*sin(EH) YgH;
    0 sin(EH) cos(EH) ZgH;
    0 0 0 1];

% %镜面追迹点在地面坐标系中的坐标%
% xmg=-sin(AH)*xm-cos(AH)*cos(EH)*ym+XgH;
% ymg=cos(AH)*xm-sin(AH)*cos(EH)*ym+YgH;
% zmg=sin(EH)*ym+ZgH;
% 
% %入射光线方程%
% (xg-xmg)/cos(ARFAi)==(yg-ymg)/cos(BETAi)==(zg-zmg)/cos(GAMAi);
% 
% %入射光线与地面Ｚｇ ＝０的交点坐标%
% xg=xmg-zmg*ctan(ARFA)*cos(A);
% yg=ymg-zmg*ctan(ARFA)*sin(A);

%阴影定日镜Ｈ ｓｈａｄｉｎｇ 在坐标系Ｘ ｏ Ｙ ｏ Ｚ ｏ 中的坐标%
Xog=107.250;
Yog=11.664;
Zog=4;

Xsg=105.360;
Ysg=23.191;
Zsg=4;

Xso=Xsg-Xog;
Yso=Ysg-Yog;
Zso=Zsg-Zog;

%地面坐标系到入射坐标系的变换矩阵%
M2=[-sin(A) cos(A) 0 0;
    -sin(ARFA)*cos(A) -sin(ARFA)*sin(A) cos(ARFA) 0;
    cos(ARFA)*cos(A) cos(ARFA)*sin(A) sin(ARFA) 0;
    0 0 0 1];

%阴影定日镜在入射坐标系中的坐标%
Xi=-Xso*sin(A)+Yso*cos(A);
Yi=-sin(ARFA)*(Xso*cos(A)+Yso*sin(A))+Zso*cos(ARFA);
Zi=cos(ARFA)*(Yso*sin(A)+Xso*cos(A))+Zso*sin(ARFA);




