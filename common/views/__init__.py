from rest_framework.viewsets import ModelViewSet as RestModelViewSet
from rest_framework.response import Response


class ModelViewSet(RestModelViewSet):
    serializer_classes = {}

    def get_serializer_class(self):
        if self.serializer_classes:
            serializer_class = self.serializer_classes.get(
                self.action, self.serializer_classes.get('default')
            )

            if isinstance(serializer_class, dict):
                serializer_class = serializer_class.get(
                    self.request.method.lower, serializer_class.get('default')
                )

            assert serializer_class, '`serializer_classes` config error'
            return serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        serializer_class = self.get_serializer_class()
        if serializer_class and hasattr(serializer_class, 'setup_eager_loading'):
            queryset = serializer_class.setup_eager_loading(queryset)
        return queryset

    def get_paginated_response_with_query_set(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
