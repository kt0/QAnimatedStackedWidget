QAnimatedStackedWidget
======================

QAnimatedStackedWidget is a Python class extends QStackedWidget functionality to animated when change widgets

## QAnimatedStackedWidget new functions :

  
####   Settings

* setSpeed(speed) : Sets duration of slide animations
* setAnimation(animationType) : Sets animation easing type ( [QEasingCurve](http://qt-project.org/doc/qt-4.8/qeasingcurve.html) )
* setVerticalMode(vertical=True) : Sets vertical mode by a Ture or False value, in vertical mode widgets slide vertically
* setWrap(wrap=True) : Sets wrap mode enabled or disabled , in wrap mode next of the last one is first one and pre of first one is last one

####   	Slidings

* slideInNext() : slide in next widget
* slideInPre() : slide in previus widget
* slideInIndex(next) : slide in defined index

