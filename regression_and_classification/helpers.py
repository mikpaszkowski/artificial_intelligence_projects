import matplotlib.pyplot as plt
import numpy


def display_plots(xgb, dt, rf, lr):
    plt.title("R² models' scores")
    plt.ylabel('R² value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.r2_score, dt.r2_score, rf.r2_score, lr.r2_score]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()

    plt.title("Models' Mean Square Error")
    plt.ylabel('MSE value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.MSE, dt.MSE, rf.MSE, lr.MSE]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()

    plt.title("Models' Mean Absolute Error")
    plt.ylabel('MAE value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.MAE, dt.MAE, rf.MAE, lr.MAE]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()

    plt.title("Models' Max Error")
    plt.ylabel('Max Error value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.ME, dt.ME, rf.ME, lr.ME]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()