from django.contrib.admin.filters import SimpleListFilter


class StatusFilter(SimpleListFilter):
    title = 'ativo'
    parameter_name = 'ativo'

    def lookups(self, request, model_admin):
        return (
            ('all', 'All'),
            (None, 'Yes'),
            ('False', 'No'),
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({self.parameter_name: lookup,}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'False':
            return queryset.filter(ativo=self.value())    
        if self.value() is None:
            return queryset.filter(ativo='True')