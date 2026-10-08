import re

with open('quotations.html', 'r') as f:
    content = f.read()

content = content.replace(
    '</select>\n                        </div>\n                      </div>',
    '</select>\n                        </div>\n                        <p class="text-xs text-muted mt-1.5">Not listed? Add them without leaving this quotation.</p>\n                      </div>'
)

content = content.replace(
    'value="QUO-0011">\n                        </div>\n                      </div>',
    'value="QUO-0011">\n                        </div>\n                        <p class="text-xs text-muted mt-1.5">Suggested next number. Assigned for good when you send.</p>\n                      </div>'
)

with open('quotations.html', 'w') as f:
    f.write(content)
