# DEPENDENCIAS NECESSARIAS
# from utilitarios.resultados import mult
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def mult(firstVar, secondVar):
    return firstVar * secondVar

# CODIGO NECESSARIO PARA A FUNÇÃO grafico_acuraria
# model.compile(metrics=['accuracy'])
#history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))
def grafico_acuracia(history):
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='lower right')

# https://stackoverflow.com/questions/7328830/image-colorization-algorithm
# https://www.geeksforgeeks.org/bresenhams-circle-drawing-algorithm/