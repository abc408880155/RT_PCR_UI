#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_btnCalculate_clicked();

    void on_btnClose_clicked();

    void on_btnReset_clicked();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
