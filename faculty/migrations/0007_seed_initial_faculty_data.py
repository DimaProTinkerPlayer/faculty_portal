from django.db import migrations


def seed_faculty_data(apps, schema_editor):
    FacultyInfo = apps.get_model('faculty', 'FacultyInfo')
    Department = apps.get_model('faculty', 'Department')
    Program = apps.get_model('faculty', 'Program')
    Teacher = apps.get_model('faculty', 'Teacher')

    FacultyInfo.objects.all().delete()
    FacultyInfo.objects.create(
        name='Факультет правничих наук Національного університету «Києво-Могилянська академія»',
        description=(
            'Факультет правничих наук НаУКМА — провідний осередок правничої освіти'
            ' України, що послідовно інтегрує континентальну правову традицію з'
            ' прецедентними підходами англо-американської юриспруденції. Академічна'
            ' філософія підрозділу ґрунтується на концепції ліберальної освіти'
            ' (Liberal Arts Education).'
        ),
        general_info=(
            'Правнича школа №1 в Україні. Середній бал вступників на бюджет — 184.'
            ' Фонд фахової бібліотеки становить 855 найменувань. Практико-орієнтоване'
            ' навчання через модельні судові процеси (Moot Courts) та Правничу клініку.'
        ),
        contact_info=(
            'Декан: Володимир Миколайович Венгер\n'
            'Телефон: +38 (044) 425-60-73\n'
            'E-mail: law@ukma.edu.ua\n'
            'Адреса: 04070, м. Київ, вул. Волоська, 8/5, 4-й корпус НаУКМА, кімн. 302'
        ),
    )

    Program.objects.all().delete()
    Teacher.objects.all().delete()
    Department.objects.all().delete()

    d1 = Department.objects.create(
        title='Кафедра загальнотеоретичного правознавства та публічного права',
        head_name='Заєць Анатолій Павлович',
    )
    d2 = Department.objects.create(
        title='Кафедра приватного права',
        head_name='Яцкевич Іван Іванович',
    )
    d3 = Department.objects.create(
        title='Кафедра кримінального та кримінального процесуального права',
        head_name='Галаган Володимир Іванович',
    )
    d4 = Department.objects.create(
        title='Кафедра міжнародного та європейського права',
        head_name='Коваль Дмитро Олександрович',
    )

    Program.objects.create(
        code='081',
        title='Бакалаврська програма «Право»',
        department=d1,
        description=(
            'Національний лідер юридичної освіти. Поєднує класичні доктрини із'
            ' західними правовими моделями, вивченням Legal English, практикою в'
            ' Правничій клініці, модельними судовими дебатами та гнучкою'
            ' індивідуальною траєкторією навчання.'
        ),
        coordinator_name='Приймальна комісія ФПН',
        coordinator_contact='vstup@ukma.edu.ua',
        disciplines=(
            'Теорія права, Історія держави і права, Конституційне право, Римське'
            ' право, Цивільне право, Адміністративне право, Кримінальне право,'
            ' Міжнародне публічне право.'
        ),
    )
    Program.objects.create(
        code='081-M',
        title='Магістерська програма «Право»',
        department=d1,
        description=(
            'Програма поглибленої підготовки фахівців судової, адвокатської та'
            ' наукової діяльності. Включає сертифікатні напрями з публічного й'
            ' комерційного права, міжнародний комерційний арбітраж.'
        ),
        coordinator_name='Деканат ФПН',
        coordinator_contact='law@ukma.edu.ua',
        disciplines=(
            'Порівняльне правознавство, Міжнародний комерційний арбітраж, Проблеми'
            ' приватного права, Практика ЄСПЛ.'
        ),
    )
    Program.objects.create(
        code='293',
        title='Докторська програма (PhD) «Міжнародне право»',
        department=d4,
        description=(
            'Підготовка докторів філософії для науково-педагогічної та нормотворчої'
            ' роботи. Дослідження сучасного міжнародного гуманітарного права та'
            ' євроінтеграції України.'
        ),
        coordinator_name='Аспірантура НаУКМА',
        coordinator_contact='law@ukma.edu.ua',
        disciplines=(
            'Методологія наукових досліджень, Міжнародне правосуддя, Міжнародне'
            ' гуманітарне право.'
        ),
    )

    teachers = [
        ('Заєць Анатолій Павлович', 'Завідувач кафедри, професор', 'Доктор юридичних наук', d1),
        ('Венгер Володимир Миколайович', 'Декан факультету, доцент', 'Кандидат юридичних наук', d1),
        ('Шевчук Станіслав Володимирович', 'Професор', 'Доктор юридичних наук', d1),
        ('Яцкевич Іван Іванович', 'Завідувач кафедри, доцент', 'Кандидат юридичних наук', d2),
        ('Музика Леся Анатоліївна', 'Професор', 'Доктор юридичних наук', d2),
        ('Галаган Володимир Іванович', 'Завідувач кафедри, професор', 'Доктор юридичних наук', d3),
        ('Хавронюк Микола Іванович', 'Професор', 'Доктор юридичних наук', d3),
        ('Коваль Дмитро Олександрович', 'Завідувач кафедри, доцент', 'Кандидат юридичних наук', d4),
        ('Петров Роман Арестович', 'Професор', 'Доктор юридичних наук', d4),
    ]
    for full_name, pos, deg, dept in teachers:
        Teacher.objects.create(full_name=full_name, position=pos, degree=deg, department=dept)


def reverse_seed_faculty_data(apps, schema_editor):
    FacultyInfo = apps.get_model('faculty', 'FacultyInfo')
    Department = apps.get_model('faculty', 'Department')
    Program = apps.get_model('faculty', 'Program')
    Teacher = apps.get_model('faculty', 'Teacher')

    Teacher.objects.all().delete()
    Program.objects.all().delete()
    Department.objects.all().delete()
    FacultyInfo.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_alter_exchangeprogram_country_and_more'),
    ]

    operations = [
        migrations.RunPython(
            code=seed_faculty_data,
            reverse_code=reverse_seed_faculty_data,
        ),
    ]