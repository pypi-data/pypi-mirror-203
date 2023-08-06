# make import easier 


# abstract modules
from HGNM.modules.abstract.AbstractInputEmbedding import AbstractInputEmbedding as AbInputEmbedding
from HGNM.modules.abstract.AbstractMessagePassingBase import AbstractMessagePassingBase as AbMessagePassingBase
from HGNM.modules.abstract.AbstractStack import AbstractStack as AbStack
from HGNM.modules.abstract.AbstractGraphAssertions import AbstractGraphAssertions as AbGraphAssertions

# heterogeneous modules
from HGNM.modules.heterogeneous.HeterogeneousInputEmbedding import HeterogeneousInputEmbedding as HeteroInputEmbedding
from HGNM.modules.heterogeneous.HeterogeneousMessagePassingBase import HeterogeneousMessagePassingBase as HeteroMessagePassingBase
from HGNM.modules.heterogeneous.HeterogeneousStack import HeterogeneousStack as HeteroStack
from HGNM.modules.heterogeneous.HeterogeneousGraphAssertions import HeterogeneousGraphAssertions as HeteroGraphAssertions

# homogeneous modules
from HGNM.modules.homogeneous.HomogeneousInputEmbedding import HomogeneousInputEmbedding as HomoInputEmbedding
from HGNM.modules.homogeneous.HomogeneousMessagePassingBase import HomogeneousMessagePassingBase as HomoMessagePassingBase
from HGNM.modules.homogeneous.HomogeneousStack import HomogeneousStack as HomoStack
from HGNM.modules.homogeneous.HomogeneousGraphAssertions import HomogeneousGraphAssertions as HomoGraphAssertions