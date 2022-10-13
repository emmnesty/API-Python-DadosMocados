import logging
from datetime import datetime

from rest_framework import serializers
from api.models import FundoImobiliario
logger = logging.getLogger(__name__)


class FundoImobiliarioSerializer(serializers.ModelSerializer):
  logger.info('Homepage was accessed at ' + str(datetime.now()) + ' hours!')

  record = FundoImobiliario(codigo=1, setor='hospital', dividend_yield_medio_12m=1, vacancia_financeira=1, vacancia_fisica=1, quantidade_ativos=1)
  record.save()

  record = FundoImobiliario(codigo=3, setor='hotel', dividend_yield_medio_12m=3, vacancia_financeira=3, vacancia_fisica=3, quantidade_ativos=3)
  record.save()



  class Meta:
    model = FundoImobiliario
    fields = [
      'id',
      'codigo',
      'setor',
      'dividend_yield_medio_12m',
      'vacancia_financeira',
      'vacancia_fisica',
      'quantidade_ativos'
    ]