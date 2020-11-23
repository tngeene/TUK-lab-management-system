from django import forms

from equipment.models import Allocation, Equipment, StorageUnit


class AllocationCreateForm(forms.ModelForm):
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.filter(
        is_allocated=False, has_exceeded_shelf_life=False, is_lost=False, is_damaged=False))

    class Meta:
        model = Allocation
        fields = ('equipment', 'allocating_to')


class EquipmentCreationForm(forms.ModelForm):
    # def __init__(self, request, *args, **kwargs):
    #         super(EquipmentCreationForm, self).__init__(request, *args, **kwargs)
    #         self.fields['storage_unit'].queryset = StorageUnit.objects.filter(lab=request.user.lab)

    class Meta:
        model = Equipment
        fields = ('name', 'serial_no', 'category', 'storage_unit', 'price')
