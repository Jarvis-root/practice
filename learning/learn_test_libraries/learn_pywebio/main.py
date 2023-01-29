import json

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *

def check_form(data):  # input group validation: return (input name, error msg) when validation fail
    if len(data['name']) > 6:
        return ('name', 'Name too long!')
    if data['age'] <= 0:
        return ('age', 'Age can not be negative!')


def check_save_doc_path(data):
    if '\\' not in data:
        return '文档保存路径错误'


def check_install_package_path(data):
    if '\\' not in data:
        return '文档保存路径错误'

def main():
    put_tabs([
        {'title': 'Text', 'content': 'Hello world'},
        {'title': 'Markdown', 'content': put_markdown('~~Strikethrough~~')},
        {'title': 'More content', 'content': [
            put_table([
                ['Commodity', 'Price'],
                ['Apple', '5.5'],
                ['Banana', '7'],
            ]),
            put_link('pywebio', 'https://github.com/wang0618/PyWebIO')
        ]},
    ])


def pin_widgets():
    put_markdown("# Pin widget")
    options = [
        {
            "label": "Option one",
            "value": 1,
            "selected": True,
        },
        {
            "label": "Option two",
            "value": 2,
        },
        {
            "label": "Disabled option",
            "value": 3,
            "disabled": True
        }
    ]

    put_input('input', label='Text input', placeholder="Enter email",
              help_text="We'll never share your email with anyone else.")
    put_input('valid_input', label="Valid input", value="correct value")
    put_input('invalid_input', label="Invalid input", value="wrong value")
    put_textarea('textarea', label='Textarea', rows=3, maxlength=10, minlength=20, value=None,
                 placeholder='This is placeholder message', readonly=False)
    put_textarea('code', label='Code area', rows=4, code={'mode': 'python'},
                 value='import pywebio\npywebio.output.put_text("hello world")')
    put_select('select', options=options, label='Select')
    put_select('select_multiple', options=options, label='Multiple select', multiple=True, value=None)
    put_checkbox('checkbox', options=options, label='Checkbox', inline=False, value=None)
    put_checkbox('checkbox_inline', options=options, label='Inline checkbox', inline=True, value=None)
    put_radio('radio', options=options, label='Radio', inline=False, value=None)
    put_radio('radio_inline', options=options, label='Inline radio', inline=True, value='B')
    put_slider('slider', label='Slider')
    put_actions('actions', buttons=[
        {'label': 'Submit', 'value': '1'},
        {'label': 'Warning', 'value': '2', 'color': 'warning'},
        {'label': 'Danger', 'value': '3', 'color': 'danger'},
    ], label='Actions')

    pin_update('valid_input', valid_status=True, valid_feedback="Success! You've done it.")
    pin_update('invalid_input', valid_status=False, invalid_feedback="Sorry, that username's taken. Try another?")


if __name__ == '__main__':
    start_server(main, debug=True, port=8088)