import os
import yaml

def main():
    create_docker_compose()

def create_docker_compose():
    docker_compose_structure = initialize_docker_compose()
    update_services(docker_compose_structure)
    write_docker_compose(docker_compose_structure)

def initialize_docker_compose():
    return {
        'version': '3.8',
        'services': {},
        'networks': {
            'docker-network': {
                'driver': 'bridge'
            }
        },
        'volumes': {}
    }

def update_services(docker_compose):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'docker-config.yml':
                with open(os.path.join(root, file), 'r') as f:
                    config = yaml.safe_load(f)
                    docker_compose['services'].update(config)
                    update_volumes(docker_compose, config)

def update_volumes(docker_compose, config):
    for service in config.values():
        if 'volumes' in service:
            for volume in service['volumes']:
                if volume.startswith('postgres'):
                    volume_name = volume.split(':')[0]
                    docker_compose['volumes'][volume_name] = {}

def write_docker_compose(docker_compose):
    with open('docker-compose.yml', 'w') as f:
        yaml.dump(docker_compose, f, sort_keys=False)

if __name__ == '__main__':
    main()