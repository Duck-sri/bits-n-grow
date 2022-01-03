from enum import Enum
from django.db.models import TextChoices

# choices as Enum
class NOTIONS(TextChoices):
  GOOD = 'good'
  BAD = 'bad'

class TIME_OF_DAY(TextChoices):
  MRNG = 'morning'
  AFN = 'afternoon'
  EVE = 'evening'
  ALL = 'all'

class MOODS(TextChoices):
  HAPPY = 'happy'
  SAD = 'sad'
  NONE = 'none'
  LOVE = 'love'
  ANGRY = 'angry'

class LOG_STATUS(TextChoices):
  COMPLETED = 'completed'
  FAIL = 'fail'
  SKIP = 'skip'

class Gender(TextChoices):
  MALE = 'Male'
  FEMALE = 'Female'
  PRIVACY = 'Preffered not to say'