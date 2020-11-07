from fitparse import FitFile, StandardUnitsDataProcessor
import pytz
import time
import os

UTC = pytz.UTC
CST = pytz.timezone('Europe/Moscow')


def data_res(filename):
    fit_file = FitFile(filename, data_processor=StandardUnitsDataProcessor())
    msgs = fit_file.messages
    total_res = {}
    for m in msgs:
        if m.name == 'file_id':
            total_res['1. Дата'] = UTC.localize(m.get_value('time_created')).astimezone(CST).strftime('%d-%m-%Y')
            total_res['3. Время начала тренировки'] = UTC.localize(m.get_value('time_created')).astimezone(CST).strftime('%H:%M:%S')
        if m.name == 'user_profile':
            if m.get_value('gender') == 'male':
                total_res['Пол'] = 'Мужчина'
            else:
                total_res['Пол'] = 'Женщина'
            total_res['Вес'] = m.get_value('weight')
            total_res['Рост'] = m.get_value('height')
        if m.name == 'session':
            total_res['2. Вид активности'] = m.get_value('sport')
            total_res['6. Длительность пауз'] = time.strftime('%H:%M:%S', time.gmtime(m.get_value('total_elapsed_time')-m.get_value('total_timer_time')))
            total_res['5. Длительность тренировки'] = time.strftime('%H:%M:%S', time.gmtime(m.get_value('total_timer_time')))
            total_res['7. Расстояние'] = str(round(m.get_value('total_distance')/1000, 2)) + ' км'
            total_res['9. Средняя скорость'] = round(m.get_value('enhanced_avg_speed'), 2)

            total_res['10. Потраченные калории'] = m.get_value('total_calories')
            total_res['8. Средний темп'] = str(time.strftime('%H:%M:%S', time.gmtime(1 / total_res['9. Средняя скорость'] * 3600))) + ' мин/км'
            total_res['11. Средняя частота пульса'] = str(m.get_value('avg_heart_rate')) + ' уд/мин'
            total_res['12. Максимальная частота пульса'] = str(m.get_value('max_heart_rate')) + ' уд/мин'
            total_res['15. Средняя длина шага'] = str(m.get_value('avg_step_length')/10) + " см"
            total_res['13. Тренировочный эффект TE'] = m.get_value('total_training_effect')
            total_res['14. Средняя амплитуда вертикальных колебаний'] = str(m.get_value('avg_vertical_oscillation')) + " мм"
            total_res['16. Отношение средней амплитуды вертикальных колебаний к средней длине шага'] = str(m.get_value('avg_vertical_ratio'))
            total_res['17. Распределение времени контакта с землей (левая нога - правая нога)'] = str(m.get_value('avg_stance_time_balance')) + '%' + ' - ' + str(100 - m.get_value('avg_stance_time_balance')) + '%'
            total_res['18. Среднее время контакта с землей'] = str(round(m.get_value('avg_stance_time'))) + ' мс'
        elif m.name == 'activity':
            total_res['4. Время окончания тренировки'] = UTC.localize(m.get_value('timestamp')).astimezone(CST).strftime('%d-%m-%Y %H:%M:%S')
    string_res = ''
    names = ('Пол', 'Вес', 'Рост', '1. Дата', '2. Вид активности', '3. Время начала тренировки', '4. Время окончания тренировки',
             '5. Длительность тренировки', '6. Длительность пауз', '7. Расстояние', '8. Средний темп',
             '9. Средняя скорость', '10. Потраченные калории', '11. Средняя частота пульса',
             '12. Максимальная частота пульса', '13. Тренировочный эффект TE',
             '14. Средняя амплитуда вертикальных колебаний', '15. Средняя длина шага',
             '16. Отношение средней амплитуды вертикальных колебаний к средней длине шага',
             '17. Распределение времени контакта с землей (левая нога - правая нога)',
             '18. Среднее время контакта с землей')

    total_res['9. Средняя скорость'] = str(total_res['9. Средняя скорость']) + ' км/ч'
    for i in names:
        string_res += i + ': ' + str(total_res[i]) + '\n'
    return string_res


def save_res(filename, path):
    f = open(path + os.path.basename(filename)[:-3] + 'txt', 'w')
    f.write(data_res(filename))
    f.close()


if __name__ == '__main__':
    print(data_res(r'D:\Training Results\A9R90207.FIT'))
