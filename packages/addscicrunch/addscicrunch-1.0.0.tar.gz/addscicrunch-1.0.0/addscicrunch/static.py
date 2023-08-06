class StaticData:
    atlas = {
        "organ" : [
            "Autonomic ganglion",
            "Brain",
            "Heart",
            "Kidney",
            "Large intestine",
            "Liver",
            "Lower urinary tract",
            "Nervous system",
            "Pancreas",
            "Peripheral nervous system",
            "Small intestine",
            "Spinal cord",
            "Spleen",
            "Stomach",
            "Sympathetic nervous system",
            "Urinary bladder",
            "colon",
            "intestine",
            "lung"
        ],
        "label" : {
            "Autonomic ganglion" : [
                "Species independent"
            ],
            "Brain" : [
                "Species Independent",
                "Berman 1968 cat brain stem atlas",
                "Allen Human Brain Atlas Terminology",
                "Cerebellar Atlas in MNI152 space after normalization with FLIRT", 
                "Cerebellar Atlas in MNI152 space after normalization with FNIRT",
                "Harvard-Oxford Cortical Structural Atlas",
                "Harvard-Oxford Subcortical Structural Atlas",
                "Human Connectome Project Multi-Modal human cortical parcellation",
                "JHU ICBM-DTI-81 White-Matter Labels",
                "JHU White-Matter Tractography Atlas",
                "Juelich Histological Atlas",
                "MNI Structural Atlas",
                "Mars Parietal connectivity-based parcellation",
                "Mars TPJ connectivity-based parcellation",
                "Neubert Ventral Frontal connectivity-based parcellation",
                "Oxford Thalamic Connectivity Probability Atlas",
                "Oxford -Imanova Striatal Connectivity Atlas 3 sub-regions",
                "Oxford -Imanova Striatal Connectivity Atlas 7 sub-regions",
                "Oxford -Imanova Striatal Structural Atlas",
                "Sallet Dorsal Frontal connectivity-based parcellation",
                "Subthalamic Nucleus Atlas",
                "Talairach Daemon Labels",
                "Allen Mouse Brain Atlas Terminology",
                "Paxinos Mouse Atlas",
                "The Mouse Brain in Stereotaxic Coordinate 2nd Edition",
                "The Mouse Brain in Stereotaxic Coordinate 3rd Edition",
                "The Mouse Brain in Stereotaxic Coordinate 4th Edition",
                "The Rat Brain in Stereotaxic Coordinates 2nd Edition",
                "The Rat Brain in Stereotaxic Coordinates 3rd Edition",
                "The Rat Brain in Stereotaxic Coordinates 4th Edition",
                "Waxholm Space Sprague Dawley Terminology v1",
                "Waxholm Space Sprague Dawley Terminology v2"
            ],
            "Heart" : [
                "Species independent"
            ],
            "Kidney" : [
                "Species independent"
            ],
            "Large intestine" : [
                "Species independent"
            ],
            "Liver" : [
                "Species independent"
            ],
            "Lower urinary tract" : [
                "Species independent"
            ],
            "Nervous system" : [
                "Species independent"
            ],
            "Pancreas" : [
                "Species independent"
            ],
            "Peripheral nervous system" : [
                "Species independent"
            ],
            "Small intestine" : [
                "Species independent"
            ],
            "Spinal cord" : [
                "Species independent"
            ],
            "Spleen" : [
                "Species independent"
            ],
            "Stomach" : [
                "Species independent"
            ],
            "Sympathetic nervous system" : [
                "Species independent"
            ],
            "Urinary bladder" : [
                "Species independent"
            ],
            "colon" : [
                "Species independent"
            ],
            "intestine" : [
                "Species independent"
            ],
            "lung" : [
                "Species independent"
            ]
        }
    }
    
    subject = {
        "species" : [
            "Felis catus",
            "Homo sapiens",
            "Mus musculus",
            "Rattus norvegicus",
            "Suncus murinus",
            "Sus scrofa"
        ],
        "sex" : [
            "Male",
            "Female",
            "Blinded to condition"
        ]
    }

    header = [
        "Filename",
        "Subject: Species",
        "Subject: ID",
        "Subject: Sex",
        "Subject: Age",
        "Atlas: Organ",
        "Atlas: Label"
    ]

    organlinks = {
        "Autonomic ganglion" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma5889"
        },
        "Brain" : {
            "Species Independent": "http://purl.org/sig/ont/fma/fma50801",
            "Berman 1968 cat brain stem atlas": "http://uri.interlex.org/berman/uris/cat/labels/",
            "Allen Human Brain Atlas Terminology": "http://uri.interlex.org/aibs/uris/human/labels/",
            "Cerebellar Atlas in MNI152 space after normalization with FLIRT": "http://uri.interlex.org/fsl/uris/atlases/Cerebellum_MNIflirt/labels/",
            "Cerebellar Atlas in MNI152 space after normalization with FNIRT": "http://uri.interlex.org/fsl/uris/atlases/Cerebellum_MNIfnirt/labels/",
            "Harvard-Oxford Cortical Structural Atlas": "http://uri.interlex.org/fsl/uris/atlases/HarvardOxford-Cortical/labels/",
            "Harvard-Oxford Subcortical Structural Atlas": "http://uri.interlex.org/fsl/uris/atlases/HarvardOxford-Subcortical/labels/",
            "Human Connectome Project Multi-Modal human cortical parcellation": "http://uri.interlex.org/hcp/uris/mmp/labels/",
            "JHU ICBM-DTI-81 White-Matter Labels": "http://uri.interlex.org/fsl/uris/atlases/JHU-labels/labels/",
            "JHU White-Matter Tractography Atlas": "http://uri.interlex.org/fsl/uris/atlases/JHU-tracts/labels/",
            "Juelich Histological Atlas": "http://uri.interlex.org/fsl/uris/atlases/Juelich/labels/",
            "MNI Structural Atlas": "http://uri.interlex.org/fsl/uris/atlases/MNI/labels/",
            "Mars Parietal connectivity-based parcellation": "http://uri.interlex.org/fsl/uris/atlases/MarsParietalParcellation/labels/",
            "Mars TPJ connectivity-based parcellation": "http://uri.interlex.org/fsl/uris/atlases/MarsTPJParcellation/labels/",
            "Neubert Ventral Frontal connectivity-based parcellation": "http://uri.interlex.org/fsl/uris/atlases/NeubertVentralFrontalParcellation/labels/",
            "Oxford Thalamic Connectivity Probability Atlas": "http://uri.interlex.org/fsl/uris/atlases/Thalamus/labels/",
            "Oxford -Imanova Striatal Connectivity Atlas 3 sub-regions": "http://uri.interlex.org/fsl/uris/atlases/Striatum-Connectivity-3sub/labels/",
            "Oxford -Imanova Striatal Connectivity Atlas 7 sub-regions": "http://uri.interlex.org/fsl/uris/atlases/Striatum-Connectivity-7sub/labels/",
            "Oxford -Imanova Striatal Structural Atlas": "http://uri.interlex.org/fsl/uris/atlases/Striatum-Structural/labels/",
            "Sallet Dorsal Frontal connectivity-based parcellation": "http://uri.interlex.org/fsl/uris/atlases/SalletDorsalFrontalParcellation/labels/",
            "Subthalamic Nucleus Atlas": "http://uri.interlex.org/fsl/uris/atlases/STN/labels/",
            "Talairach Daemon Labels": "http://uri.interlex.org/fsl/uris/atlases/Talairach/labels/",
            "Allen Mouse Brain Atlas Terminology": "http://uri.interlex.org/aibs/uris/mouse/labels/",
            "Paxinos Mouse Atlas": "http://uri.interlex.org/paxinos/uris/mouse/labels/",
            "The Mouse Brain in Stereotaxic Coordinate 2nd Edition": "http://uri.interlex.org/paxinos/uris/mouse/labels/",
            "The Mouse Brain in Stereotaxic Coordinate 3rd Edition": "http://uri.interlex.org/paxinos/uris/mouse/labels/",
            "The Mouse Brain in Stereotaxic Coordinate 4th Edition": "http://uri.interlex.org/paxinos/uris/mouse/labels/",
            "The Rat Brain in Stereotaxic Coordinates 2nd Edition": "http://uri.interlex.org/paxinos/uris/rat/labels/",
            "The Rat Brain in Stereotaxic Coordinates 3rd Edition": "http://uri.interlex.org/paxinos/uris/rat/labels/",
            "The Rat Brain in Stereotaxic Coordinates 4th Edition": "http://uri.interlex.org/paxinos/uris/rat/labels/",
            "Waxholm Space Sprague Dawley Terminology v1": "http://uri.interlex.org/waxholm/uris/sd/labels/",
            "Waxholm Space Sprague Dawley Terminology v2": "http://uri.interlex.org/waxholm/uris/sd/labels/"
        },
        "Heart" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7088"
        },
        "Kidney" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7203"
        },
        "Large intestine" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7201"
        },
        "Liver" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7197"
        },
        "Lower urinary tract" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma45659"
        },
        "Nervous system" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7157"
        },
        "Pancreas" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7198"
        },
        "Peripheral nervous system" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma9903"
        },
        "Small intestine" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7200"
        },
        "Spinal cord" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7647"
        },
        "Spleen" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7196"
        },
        "Stomach" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7148"
        },
        "Sympathetic nervous system" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma9906"
        },
        "Urinary bladder" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma15900"
        },
        "colon" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma14543"
        },
        "intestine" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7199"
        },
        "lung" : {
            "Species independent": "http://purl.org/sig/ont/fma/fma7195"
        }
    }

    specieslinks = {
        "forward" : {
            "Felis catus": "http://purl.obolibrary.org/obo/NCBITaxon_9685",
            "Homo sapiens": "http://purl.obolibrary.org/obo/NCBITaxon_9606",
            "Mus musculus": "http://purl.obolibrary.org/obo/NCBITaxon_10090",
            "Rattus norvegicus": "http://purl.obolibrary.org/obo/NCBITaxon_10116",
            "Suncus murinus": "http://purl.obolibrary.org/obo/NCBITaxon_9378",
            "Sus scrofa": "http://purl.obolibrary.org/obo/NCBITaxon_9823"
        },
        "reverse" : {
            "http://purl.obolibrary.org/obo/NCBITaxon_9685": "Felis catus",
            "http://purl.obolibrary.org/obo/NCBITaxon_9606": "Homo sapiens",
            "http://purl.obolibrary.org/obo/NCBITaxon_10090": "Mus musculus",
            "http://purl.obolibrary.org/obo/NCBITaxon_10116": "Rattus norvegicus",
            "http://purl.obolibrary.org/obo/NCBITaxon_9378": "Suncus murinus",
            "http://purl.obolibrary.org/obo/NCBITaxon_9823": "Sus scrofa"
        }
    }
