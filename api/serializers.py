import logging
from datetime import datetime

from rest_framework import serializers
from api.models import FundoImobiliario
logger = logging.getLogger(__name__)


class FundoImobiliarioSerializer(serializers.ModelSerializer):
  logger.info('Homepage was accessed at ' + str(datetime.now()) + ' hours!')

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