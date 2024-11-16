{"filter":false,"title":"wsgi.py","tooltip":"/django_ecommerce_project/ecommerce_project/wsgi.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":47},"action":"insert","lines":["from django.apps import AppConfig","from .cloudwatch_utils import create_log_stream"],"id":13}],[{"start":{"row":3,"column":49},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":47},"action":"remove","lines":["from django.apps import AppConfig","from .cloudwatch_utils import create_log_stream"],"id":11}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":20},"action":"remove","lines":["class ElectronicConfig(AppConfig):","    name = 'electronic'","","    def ready(self):"],"id":10},{"start":{"row":12,"column":0},"end":{"row":17,"column":27},"action":"insert","lines":["class ElectronicConfig(AppConfig):","    name = 'electronic'","","    def ready(self):","        # Run log stream creation at startup","        create_log_stream()"]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["    "],"id":9}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":[" "],"id":8}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "],"id":7},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":[" "]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":[" "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":[" "]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":[" "]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":[" "]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":[" "]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":[" "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "],"id":5},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":[" "]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":4}],[{"start":{"row":9,"column":0},"end":{"row":15,"column":20},"action":"insert","lines":["from django.apps import AppConfig","from .cloudwatch_utils import create_log_stream","","class ElectronicConfig(AppConfig):","    name = 'electronic'","","    def ready(self):"],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":0},"end":{"row":9,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1731522592226,"hash":"ec67928b28653844051cb6153c698df0358a9bbf"}