{'turn_on': Service(
    service_id='turn_on',
    name='Turn on',
    description='Turn on one or more lights and adjust properties of the light, even when they are turned on already.',
    fields={
        'transition': ServiceField(
            description='Duration it takes to get to next state.',
            example=None,
            selector={
                'number': {
                    'min': 0,
                    'max': 300,
                    'unit_of_measurement': 'seconds'
                }
            },
            name='Transition',
            required=None
        ),
        'rgb_color': ServiceField(
            description='The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.',
            example=None,
            selector={
                'color_rgb': None
            },
            name='Color',
            required=None
        ),
        'rgbw_color': ServiceField(
            description='The color in RGBW format. A list of four integers between 0 and 255 representing the values of red, green, blue, and white.',
            example='[255, 100, 100, 50]',
            selector={
                'object': None
            },
            name='RGBW-color',
            required=None
        ),
        'rgbww_color': ServiceField(
            description='The color in RGBWW format. A list of five integers between 0 and 255 representing the values of red, green, blue, cold white, and warm white.',
            example='[255, 100, 100, 50, 70]',
            selector={'object': None},
            name='RGBWW-color',
            required=None),
        'color_name': ServiceField(
            description='A human-readable color name.',
            example=None,
            selector={'select': {'translation_key': 'color_name',
                                 'options': ['homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']}}, name='Color name', required=None), 'hs_color': ServiceField(description='Color in hue/sat format. A list of two integers. Hue is 0-360 and Sat is 0-100.', example='[300, 70]', selector={'object': None}, name='Hue/Sat color', required=None), 'xy_color': ServiceField(description='Color in XY-format. A list of two decimal numbers between 0 and 1.', example='[0.52, 0.43]', selector={'object': None}, name='XY-color', required=None), 'color_temp': ServiceField(description='Color temperature in mireds.', example=None, selector={'color_temp': {'min_mireds': 153, 'max_mireds': 500}}, name='Color temperature', required=None), 'kelvin': ServiceField(description='Color temperature in Kelvin.', example=None, selector={'number': {'min': 2000, 'max': 6500, 'step': 100, 'unit_of_measurement': 'K'}}, name='Color temperature', required=None), 'brightness': ServiceField(description='Number indicating brightness, where 0 turns the light off, 1 is the minimum brightness, and 255 is the maximum brightness.', example=None, selector={'number': {'min': 0, 'max': 255}}, name='Brightness value', required=None), 'brightness_pct': ServiceField(description='Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.', example=None, selector={'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}, name='Brightness', required=None), 'brightness_step': ServiceField(description='Change brightness by an amount.', example=None, selector={'number': {'min': -225, 'max': 255}}, name='Brightness step value', required=None), 'brightness_step_pct': ServiceField(description='Change brightness by a percentage.', example=None, selector={'number': {'min': -100, 'max': 100, 'unit_of_measurement': '%'}}, name='Brightness step', required=None), 'white': ServiceField(description='Set the light to white mode.', example=None, selector={'constant': {'value': True, 'label': 'Enabled'}}, name='White', required=None), 'profile': ServiceField(description='Name of a light profile to use.', example='relax', selector={'text': None}, name='Profile', required=None), 'flash': ServiceField(description='If the light should flash.', example=None, selector={'select': {'options': [
                                     {'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}, name='Flash', required=None), 'effect': ServiceField(description='Light effect.', example=None, selector={'text': None}, name='Effect', required=None)}), 'turn_off': Service(service_id='turn_off', name='Turn off', description='Turn off one or more lights.', fields={'transition': ServiceField(description='Duration it takes to get to next state.', example=None, selector={'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}, name='Transition', required=None), 'flash': ServiceField(description='If the light should flash.', example=None, selector={'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}, name='Flash', required=None)}), 'toggle': Service(service_id='toggle', name='Toggle', description='Toggles one or more lights, from on to off, or, off to on, based on their current state.', fields={'transition': ServiceField(description='Duration it takes to get to next state.', example=None, selector={'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}, name='Transition', required=None), 'rgb_color': ServiceField(description='The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.', example='[255, 100, 100]', selector={'object': None}, name='Color', required=None), 'color_name': ServiceField(description='A human-readable color name.', example=None, selector={'select': {'translation_key': 'color_name', 'options': ['homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']}}, name='Color name', required=None), 'hs_color': ServiceField(description='Color in hue/sat format. A list of two integers. Hue is 0-360 and Sat is 0-100.', example='[300, 70]', selector={'object': None}, name='Hue/Sat color', required=None), 'xy_color': ServiceField(description='Color in XY-format. A list of two decimal numbers between 0 and 1.', example='[0.52, 0.43]', selector={'object': None}, name='XY-color', required=None), 'color_temp': ServiceField(description='Color temperature in mireds.', example=None, selector={'color_temp': None}, name='Color temperature', required=None), 'kelvin': ServiceField(description='Color temperature in Kelvin.', example=None, selector={'number': {'min': 2000, 'max': 6500, 'step': 100, 'unit_of_measurement': 'K'}}, name='Color temperature', required=None), 'brightness': ServiceField(description='Number indicating brightness, where 0 turns the light off, 1 is the minimum brightness, and 255 is the maximum brightness.', example=None, selector={'number': {'min': 0, 'max': 255}}, name='Brightness value', required=None), 'brightness_pct': ServiceField(description='Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.', example=None, selector={'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}, name='Brightness', required=None), 'white': ServiceField(description='Set the light to white mode.', example=None, selector={'constant': {'value': True, 'label': 'Enabled'}}, name='White', required=None), 'profile': ServiceField(description='Name of a light profile to use.', example='relax', selector={'text': None}, name='Profile', required=None), 'flash': ServiceField(description='If the light should flash.', example=None, selector={'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}, name='Flash', required=None), 'effect': ServiceField(description='Light effect.', example=None, selector={'text': None}, name='Effect', required=None)})}
