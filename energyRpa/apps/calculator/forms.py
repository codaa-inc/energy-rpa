from django import forms
from .models import CalcUvalueTmpl

class CalcUvalueTmplForm(forms.ModelForm):
    class Meta:
        model = CalcUvalueTmpl
        fields = ['purps_cd', 'area_gb_cd', 'username', 'wall_direct_kind_1', 'wall_direct_thick_1',
                  'wall_direct_width', 'wall_indirect_kind_1', 'wall_indirect_thick_1', 'wall_indirect_width',
                  'wall_direct_kind_2', 'wall_direct_thick_2', 'wall_indirect_kind_2', 'wall_indirect_thick_2',
                  'wall_direct_kind_3', 'wall_direct_thick_3', 'wall_indirect_kind_3', 'wall_indirect_thick_3',
                  'wall_direct_kind_4', 'wall_direct_thick_4', 'wall_indirect_kind_4', 'wall_indirect_thick_4',
                  'win_direct_kind_1', 'win_indirect_kind_1', 'win_direct_width', 'win_indirect_width',
                  'roof_direct_kind_1', 'roof_direct_thick_1', 'roof_indirect_kind_1', 'roof_indirect_thick_1',
                  'roof_direct_kind_2', 'roof_direct_thick_2', 'roof_indirect_kind_2', 'roof_indirect_thick_2',
                  'roof_direct_kind_3', 'roof_direct_thick_3', 'roof_indirect_kind_3', 'roof_indirect_thick_3',
                  'floorb_direct_kind_1', 'floorb_direct_thick_1', 'floorb_indirect_kind_1', 'floorb_indirect_thick_1',
                  'floorb_direct_width',  'floorb_indirect_width', 'floorb_direct_kind_2', 'floorb_direct_thick_2',
                  'floorb_indirect_kind_2', 'floorb_indirect_thick_2', 'floor_direct_kind_1', 'floor_direct_thick_1',
                  'floor_direct_width', 'floor_indirect_kind_1', 'floor_indirect_thick_1', 'floor_indirect_width',
                  'floor_direct_kind_2', 'floor_direct_thick_2', 'floor_indirect_kind_2', 'floor_indirect_thick_2',
                  'floor_direct_kind_3', 'floor_direct_thick_3', 'floor_indirect_kind_3', 'floor_indirect_thick_3',
                  'floor_direct_kind_4', 'floor_direct_thick_4', 'floor_indirect_kind_4', 'floor_indirect_thick_4',
                  'floor_direct_kind_5', 'floor_direct_thick_5', 'floor_indirect_kind_5', 'floor_indirect_thick_5']
