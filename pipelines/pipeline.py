import kfp
from kfp import components
from kfp import dsl

preprocess_op = components.load_component_from_url(
    'https://ishii-test-upload.oss-ap-northeast-1.aliyuncs.com/kfp/components/component.yaml'
)

@dsl.pipeline(
    name='Preprocess only pipeline',
    description='This pipeline preprocess the data.'
)
def my_pipeline(
    bucket_name='{{oss-bucketname}}',
    output_dir_path='{{output-dir}}',
    input_file_path='{{raw-filename}}',
    oss_endpoint='oss-ap-northeast-1.aliyuncs.com',
    access_key='{{accesskey}}',
    access_key_secret='{{accesskeysecret}}'
):
    _prepro_task = preprocess_op(
        filename=input_file_path,
        output=output_dir_path,
        bucketname=bucket_name,
        endpoint=oss_endpoint,
        accesskey=access_key,
        accesskeysecret=access_key_secret
    )
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(my_pipeline, arguments={})