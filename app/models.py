from django.db import models

# Create your models here.

class doctors_data(models.Model):
    doctor_name = models.CharField(max_length=50)
    education = models.CharField(max_length=200)
    consultant = models.CharField(max_length=200)
    disease = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.doctor_name

# class mri_patient_data(models.Model):
#     patient_first_name = models.CharField(max_length=50)
#     patient_last_name = models.CharField(max_length=50)
#     patient_contact = models.PositiveIntegerField()
#     patient_age = models.PositiveIntegerField()
#     uploaded_mri = models.ImageField()
#     prediction = models.CharField(max_length=50)
#     doctor = models.CharField(max_length=500)
#     date = models.DateField()

#     def __str__(self):
#         return self.patient_first_name + " " + self.patient_last_name


class Patient_data(models.Model):
    MY_CHOICES = (
        ('default' , 'Select Symptom'),
        ('0' , 'Itching'),
        ('1' , 'Skin Rash'),
        ('2' , 'Nodal Skin Eruptions'),
        ('3' , 'Continuous Sneezing'),
        ('4' , 'Shivering'),
        ('5' , 'Chills'),
        ('6' , 'Joint Pain'),
        ('7' , 'Stomach Pain'),
        ('8' , 'Acidity'),
        ('9' , 'Ulcers on Tongue'),
        ('10' , 'Muscle_ Wsting'),
        ('11' , 'Vomiting'),
        ('12' , 'Burning Micturition'),
        ('13' , 'Spotting Urination'),
        ('14' , 'Fatigue'),
        ('15' , 'Weight Gain'),
        ('16' , 'Anxiety'),
        ('17' , 'Cold Hands and Feets'),
        ('18' , 'Mood Swings'),
        ('19' , 'Weight Loss'),
        ('20' , 'Restlessness'),
        ('21' , 'Lethargy'),
        ('22' , 'Patches in Throat'),
        ('23' , 'Irregular Sugar Level'),
        ('24' , 'Cough'),
        ('25' , 'High Fever'),
        ('26' , 'Sunken Eyes'),
        ('27' , 'Breathlessness'),
        ('28' , 'Sweating'),
        ('29' , 'Dehydration'),
        ('30' , 'Indigestion'),
        ('31' , 'Headache'),
        ('32' , 'Yellowish Skin'),
        ('33' , 'Dark Urine'),
        ('34' , 'Nausea'),
        ('35' , 'Loss of Appetite'),
        ('36' , 'Pain behind the Eyes'),
        ('37' , 'Back Pain'),
        ('38' , 'Constipation'),
        ('39' , 'Abdominal Pain'),
        ('40' , 'Diarrhoea'),
        ('41' , 'Mild Fever'),
        ('42' , 'Yellow Urine'),
        ('43' , 'Yellowing of eyes'),
        ('44' , 'Acute Liver Failure'),
        ('45' , 'Fluid Overload'),
        ('46' , 'Swelling of Stomach'),
        ('47' , 'Swelled Lymph Nodes'),
        ('48' , 'Blurred and Distorted Vision'),
        ('49' , 'Phlegm'),
        ('50' , 'Throat Irritation'),
        ('51' , 'Redness of eyes'),
        ('52' , 'Sinus pressure'),
        ('53' , 'Runny Nose'),
        ('54' , 'Congestion'),
        ('55' , 'Chest pain'),
        ('56' , 'Weakness in limbs'),
        ('57' , 'Fast Heart Rate'),
        ('58' , 'Pain during bowel Movements'),
        ('59' , 'Pain in anal region'),
        ('60' , 'Bloody Stool'),
        ('61' , 'Irritation in Anus'),
        ('62' , 'Neck pain'),
        ('63' , 'Dizziness'),
        ('64' , 'Bruising'),
        ('65' , 'Obesity'),
        ('66' , 'Swollen legs'),
        ('67' , 'Swollen Blood Vessels'),
        ('68' , 'Puffy face and eyes'),
        ('69' , 'Enlarged Thyroid'),
        ('70' , 'Brittle Nails'),
        ('71' , 'Swollen Extremeties'),
        ('72' , 'excessive hunger'),
        ('73' , 'extra marital contacts'),
        ('74' , 'drying and tingling lips'),
        ('75' , 'slurred speech'),
        ('76' , 'knee pain'),
        ('77' , 'hip joint pain'),
        ('78' , 'muscle weakness'),
        ('79' , 'stiff neck'),
        ('80' , 'swelling joints'),
        ('81' , 'movement stiffness'),
        ('82' , 'spinning movements'),
        ('83' , 'loss of balance'),
        ('84' , 'unsteadiness'),
        ('85' , 'weakness of one body side'),
        ('86' , 'loss of smell'),
        ('87' , 'bladder discomfort'),
        ('88' , 'foul smell of'),
        ('89' , 'continuous feel of urine'),
        ('90' , 'passage of gases'),
        ('91' , 'internal itching'),
        ('92' , 'toxic look (typhos)'),
        ('93' , 'depression'),
        ('94' , 'irritability'),
        ('95' , 'muscle pain'),
        ('96' , 'altered sensorium'),
        ('97' , 'red spots over body'),
        ('98' , 'belly pain'),
        ('99' , 'abnormal menstruation'),
        ('100' , 'dischromic'),
        ('101' , 'watering from eyes'),
        ('102' , 'increased appetite'),
        ('103' , 'polyuria'),
        ('104' , 'family history'),
        ('105' , 'mucoid sputum'),
        ('106' , 'rusty sputum'),
        ('107' , 'lack of concentration'),
        ('108' , 'visual disturbances'),
        ('109' , 'receiving blood transfusion'),
        ('110' , 'receiving unsterile injections'),
        ('111' , 'coma'),
        ('112' , 'stomach bleeding'),
        ('113' , 'distention of abdomen'),
        ('114' , 'history of alcohol consumption'),
        ('115' , 'fluid overload'),
        ('116' , 'blood in sputum'),
        ('117' , 'prominent veins on calf'),
        ('118' , 'palpitations'),
        ('119' , 'painful walking'),
        ('120' , 'pus filled pimples'),
        ('121' , 'blackheads'),
        ('122' , 'scurring'),
        ('123' , 'skin peeling'),
        ('124' , 'silver like dusting'),
        ('125' , 'small dents in nails'),
        ('126' , 'inflammatory nails'),
        ('127' , 'blister'),
        ('128' , 'red sore around nose'),
        ('129' , 'yellow crust ooze'),
    )
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_contact = models.PositiveIntegerField()
    patient_age = models.PositiveIntegerField()
    patient_sym1 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym2 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym3 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym4 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym5 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym6 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym7 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym8 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym9 = models.CharField(max_length=50, choices=MY_CHOICES)
    patient_sym10 = models.CharField(max_length=50, choices=MY_CHOICES)
    prediction = models.CharField(max_length=50)
    doctor = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.patient_first_name + " " + self.patient_last_name