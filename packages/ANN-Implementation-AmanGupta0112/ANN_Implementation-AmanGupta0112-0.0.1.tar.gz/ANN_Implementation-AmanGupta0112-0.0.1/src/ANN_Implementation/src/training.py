import argparse
from ANN_Implementation.src.utils.common import read_config
from ANN_Implementation.src.utils.data_mgmt import (get_data,
                                save_model, 
                                plot_data, 
                                predict, 
                                get_log_path, 
                                create_log, 
                                callback_function, 
                                train_model_checkpoint)
from ANN_Implementation.src.utils.models import create_model

def training_data(config_path):
    config = read_config(config_path)
    validation_datasize = config['params']['validation_datasize']
    NUM_CLASSES = config['params']['no_classes']
    OPTIMIZER = config['params']['optimizer']
    METRICS = config['params']['metrics']
    LOSS_FN = config['params']['loss_function']
    EPOCHS = config['params']['epochs']
    MODEL_DIR = config['artifacts']['model_dir']
    ARTIFACT_DIR = config['artifacts']['artifacts_dir']
    MODEL_NAME = config['artifacts']['model_name']
    PLOT_DIR = config['artifacts']['plots_dir']
    PLOT_NAME = config['artifacts']['plot_name']
    PREDICTION_IMAGE = config['artifacts']['prediction_image_dir']
    CKPT_MODEL = config['artifacts']['checkpoint_model']



    

    (x_train, y_train), (x_valid, y_valid), (x_test,
                                             y_test) = get_data(validation_datasize)
    log_dir = get_log_path()
    create_log(log_dir, x_train)
    CallBack_list = callback_function(log_dir, ARTIFACT_DIR, CKPT_MODEL)
    
    model = create_model(LOSS_FN, OPTIMIZER, METRICS,
                         NUM_CLASSES)
    VALIDATION = (x_valid, y_valid)

    history = model.fit(x_train, y_train, epochs=EPOCHS,
                        validation_data=VALIDATION, callbacks=CallBack_list)
    
    history2 = train_model_checkpoint(ARTIFACT_DIR, CKPT_MODEL,
                           EPOCHS, x_train, y_train, VALIDATION, CallBack_list)

    file_name = save_model(model, ARTIFACT_DIR, MODEL_DIR, MODEL_NAME)
    plot_data(history, ARTIFACT_DIR, PLOT_DIR, PLOT_NAME)
    predict(ARTIFACT_DIR, MODEL_DIR, file_name,
            PLOT_DIR, PREDICTION_IMAGE, x_test, y_test)
    


    



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    import pdb
    pdb.set_trace()
    args.add_argument("--config","-c",default="config.yml")
    parsed_args = args.parse_args()
    training_data(config_path=parsed_args.config)
