import yaml


class Settings:
  def __init__(self):
    self.__data_path = ''
    self.__solver_method = ''
    self.__pdm_plot_settings = {}

  def get_data_path(self):
    return self.__data_path
  
  def get_solver_method(self):
    return self.__solver_method
  
  def get_pdm_plot_settings(self):
    return self.__pdm_plot_settings
  
  def import_settings_from_txt_file(self, settings_extension = ""):
    print('Importing settings...')
    with open('settings.yaml', 'r') as file:
      settings_yaml = yaml.safe_load(file)
      
      self.__data_path = settings_yaml['data_path']
      self.__solver_method = settings_yaml['solver_method']
      self.__pdm_plot_settings = {
        "plot_djikstra" : settings_yaml['pdm_plot_settings']['plot_djikstra'],
        "plot_pdm" : settings_yaml['pdm_plot_settings']['plot_pdm'],
        "plot_final": settings_yaml['pdm_plot_settings']['plot_final']
      }
