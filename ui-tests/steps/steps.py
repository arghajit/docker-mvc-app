
SELECTOR_COUNT_BOX = ''
SELECTOR_BUTTON_BY_TEXT = ''
SELECTOR_CARDS_NAME = ''

@when('we visit google')
def step(context):
   context.browser.get('http://www.google.com')

@then('it should have a title "Google"')
def step(context):
   assert context.browser.title == "Google"

@when(u'we visit "{url}"')
def step_impl(context, url):
    context.browser.get(url)

@then(u'it should have a title "{title}"')
def step_impl(context, title):
    assert context.browser.title == title

@then(u'user count is visible in UI')
def step_impl(context):
    try:
        assert context.browser.find_element_by_css_selector(SELECTOR_COUNT_BOX).is_displayed()
    except:
        assert False

@then(u'user count shows there are "{count}" users')
def step_impl(context, count):
    try:
        assert context.browser.find_element_by_css_selector(SELECTOR_COUNT_BOX).text() == count
    except:
        assert False

@when(u'click on "{button}" button')
@when(u'user click on the "{button}" button')
def step_impl(context, button):
    try:
        context.browser.find_element_by_css_selector(SELECTOR_BUTTON_BY_TEXT.format(button)).click()
    except:
        assert False
    assert True

@then(u'user can see a button with text "{button}"')
def step_impl(context, button):
    try:
        context.browser.find_element_by_css_selector(SELECTOR_BUTTON_BY_TEXT.format(button)).is_displayed()
    except:
        assert False
    assert True

@then(u'user can see UI showing fields "{labels}" in this order')
def step_impl(context, labels):
    raise NotImplementedError(u'STEP: Then user can see UI showing fields "Name, Email, Birthday, Address" in this order')

@when(u'user feel {data} in form')
def step_impl(context, data):
    raise NotImplementedError(u'STEP: When user feel data in form')

@then(u'there are 1 records in UI')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then there are 1 records in UI')


@when(u'user click on any users')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user click on any users')


@when(u'user click on user panel containing name "{name}"')
def step_impl(context, name):
    try:
        context.browser.find_elements_by_css_selector(SELECTOR_CARDS_NAME.format(name)).click()
    except:
        assert False
    assert True

@then(u'user can see UI showing fields "{labels}" in this order with {data}')
def step_impl(context,labels,data):
    raise NotImplementedError(u'STEP: Then user can see UI showing fields "Name, Email, Birthday, Address" in this order with data')
