__author__ = 'kito'


from PySide.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QParallelAnimationGroup
from PySide.QtGui import QStackedWidget


class QAnimatedStackedWidget(QStackedWidget):
    def __init__(self,parent=None):
        super(QAnimatedStackedWidget,self).__init__(parent)
        self.initElements()

    def initElements(self):
        self.speed = 500
        self.animationType = QEasingCurve.OutCubic
        self.now = 0
        self.next = 1
        self.wrap = False
        self.activeState = False
        self.blockedPageList = []
        self.vertical = False

    def setSpeed(self,speed):
        self.speed = speed
    def setAnimation(self,animationType): # animationType is QEasingCurve
        self.animationType = animationType
    def setVerticalMode(self,vertical=True):
        self.vertical = vertical
    def setWrap(self,wrap):
        self.wrap = wrap

    def slideInNext(self):
        now = self.currentIndex()
        if self.wrap or now<self.count()-1:
            self.slideInIndex(now+1)
    def slideInPrev(self):
        now = self.currentIndex()
        if self.wrap or now>0:
            self.slideInIndex(now-1)
    def slideInIndex(self,next):
        now = self.currentIndex()
        if self.activeState or next == now :
            return
        self.activeState = True
        width , height = self.frameRect().width() , self.frameRect().height()
        next %= self.count()
        if next > now:
            if self.vertical:
                offsetx , offsety = 0 , height
            else:
                offsetx , offsety = width , 0
        elif next<now:
            if self.vertical:
                offsetx , offsety = 0 , -height
            else:
                offsetx , offsety = -width , 0
        self.widget(next).setGeometry(0,  0, width, height)
        pnow , pnext = self.widget(now).pos() , self.widget(next).pos()
        self.pointNow = pnow

        self.widget(next).move(pnext.x()+offsetx,pnext.y()+offsety)
        self.widget(next).show()
        self.widget(next).raise_()

        animnow = QPropertyAnimation(self.widget(now),'pos')
        animnow.setDuration(self.speed)
        animnow.setStartValue(pnow)
        animnow.setEndValue(QPoint(pnow.x()-offsetx,pnow.y()-offsety))
        animnow.setEasingCurve(self.animationType)

        animnext = QPropertyAnimation(self.widget(next),'pos')
        animnext.setDuration(self.speed)
        animnext.setStartValue(QPoint(offsetx+pnext.x(),offsety+pnext.y()))
        animnext.setEndValue(pnext)
        animnext.setEasingCurve(self.animationType)

        self.animGroup = QParallelAnimationGroup()
        self.animGroup.addAnimation(animnow)
        self.animGroup.addAnimation(animnext)
        self.animGroup.finished.connect(self.__animationDoneSlot)
        self.animGroup.start()

        self.next = next
        self.now = now

    def __animationDoneSlot(self):
        self.setCurrentIndex(self.next)
        self.widget(self.now).hide()
        self.widget(self.now).move(self.pointNow)
        self.widget(self.now).update()
        self.activeState = False
        # emit animationFinished Signal ( don't know how to do that )
