# task-manager-new-day

# next to implement:
def get_success_url(self):
        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return referer
        return reverse_lazy("task-manager:task-list")