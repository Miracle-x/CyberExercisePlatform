from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.kubernetes_service import KubernetesService

router = APIRouter()

kubernetes_service = KubernetesService()

class EnvironmentCreateRequest(BaseModel):
    namespace: str
    image: str
    name: str

@router.post("/environment")
def create_environment(request: EnvironmentCreateRequest):
    try:
        # 创建Kubernetes命名空间
        kubernetes_service.create_namespace(request.namespace)
        # 在命名空间中创建Pod
        kubernetes_service.create_pod(request.namespace, request.name, request.image)
        return {"message": "Environment created", "namespace": request.namespace, "pod_name": request.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/environment/{namespace}")
def delete_environment(namespace: str):
    try:
        # 删除Kubernetes命名空间及其所有资源
        kubernetes_service.delete_namespace(namespace)
        return {"message": "Environment deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
