RECOMMENDATIONS = {

    # ─── APPLE ───────────────────────────────────────────────────────────────
    'Apple___Apple_scab': {
        'description': 'Tavelure du pommier causée par le champignon Venturia inaequalis. Provoque des taches brunes sur feuilles et fruits.',
        'traitement': [
            'Appliquer un fongicide à base de cuivre ou de soufre dès les premiers symptômes',
            'Utiliser des fongicides systémiques (triazoles, strobilurines)',
            'Répéter le traitement toutes les 7-10 jours en période humide',
            'Retirer et détruire les feuilles et fruits atteints',
        ],
        'prevention': [
            'Ramasser et détruire les feuilles tombées en automne',
            'Tailler pour améliorer la circulation d\'air dans l\'arbre',
            'Choisir des variétés résistantes à la tavelure',
            'Éviter l\'arrosage par aspersion sur le feuillage',
        ],
        'urgence': 'moyenne',
    },

    'Apple___Black_rot': {
        'description': 'Pourriture noire du pommier causée par Botryosphaeria obtusa. Provoque des pourritures sur fruits, chancres sur branches.',
        'traitement': [
            'Retirer et détruire immédiatement tous les fruits et branches infectés',
            'Appliquer un fongicide homologué (captan, myclobutanil)',
            'Désinfecter soigneusement les outils de taille à l\'alcool',
            'Traiter les plaies de taille avec un produit cicatrisant',
        ],
        'prevention': [
            'Bonne gestion et élimination des débris végétaux',
            'Éviter les blessures sur l\'écorce lors des travaux',
            'Maintenir les arbres en bonne santé par une fertilisation équilibrée',
            'Surveiller régulièrement après les épisodes de grêle',
        ],
        'urgence': 'haute',
    },

    'Apple___Cedar_apple_rust': {
        'description': 'Rouille du pommier causée par Gymnosporangium juniperi-virginianae. Taches orange vif sur les feuilles.',
        'traitement': [
            'Appliquer un fongicide à base de myclobutanil ou de triazole',
            'Traiter dès l\'apparition des taches orange au printemps',
            'Répéter toutes les 7-10 jours pendant la période de contamination',
        ],
        'prevention': [
            'Éliminer les genévriers et cèdres proches (hôtes alternatifs)',
            'Choisir des variétés de pommiers résistantes',
            'Traitement préventif au printemps avant la floraison',
            'Surveiller les genévriers pour détecter les galles orange',
        ],
        'urgence': 'moyenne',
    },

    'Apple___healthy': {
        'description': '✅ Votre pommier est en parfaite santé ! Continuez vos bonnes pratiques.',
        'traitement': [],
        'prevention': [
            'Continuer les traitements préventifs saisonniers',
            'Surveiller régulièrement le feuillage et les fruits',
            'Fertilisation équilibrée (azote, potasse, phosphore)',
            'Taille annuelle pour maintenir une bonne aération',
        ],
        'urgence': 'aucune',
    },

    # ─── BLUEBERRY ───────────────────────────────────────────────────────────
    'Blueberry___healthy': {
        'description': '✅ Votre myrtillier est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Maintenir un sol acide (pH 4.5-5.5)',
            'Arrosage régulier, éviter les excès d\'eau',
            'Pailler le pied pour conserver l\'humidité',
            'Surveiller l\'apparition de maladies fongiques',
        ],
        'urgence': 'aucune',
    },

    # ─── CHERRY ──────────────────────────────────────────────────────────────
    'Cherry_(including_sour)___Powdery_mildew': {
        'description': 'Oïdium du cerisier causé par Podosphaera clandestina. Feuilles et jeunes pousses couvertes d\'un feutrage blanc.',
        'traitement': [
            'Appliquer du soufre mouillable dès l\'apparition des symptômes',
            'Utiliser un fongicide systémique (triazole, myclobutanil)',
            'Traiter toutes les 10-14 jours jusqu\'à disparition',
            'Supprimer les pousses très atteintes',
        ],
        'prevention': [
            'Bonne aération par taille régulière',
            'Éviter les excès d\'engrais azotés (favorisent les pousses tendres)',
            'Traitement préventif au soufre en début de saison',
            'Choisir des variétés moins sensibles',
        ],
        'urgence': 'moyenne',
    },

    'Cherry_(including_sour)___healthy': {
        'description': '✅ Votre cerisier est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Taille annuelle après la récolte',
            'Traitement préventif hivernal (huile blanche)',
            'Surveiller les pucerons au printemps',
            'Fertilisation modérée en azote',
        ],
        'urgence': 'aucune',
    },

    # ─── CORN (MAIZE) ────────────────────────────────────────────────────────
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'description': 'Cercosporiose du maïs causée par Cercospora zeae-maydis. Taches grises allongées sur les feuilles réduisant la photosynthèse.',
        'traitement': [
            'Appliquer un fongicide triazole ou strobilurine en début d\'infection',
            'Traiter au stade floraison pour protéger les feuilles supérieures',
            'Répéter si les conditions humides persistent',
        ],
        'prevention': [
            'Rotation des cultures (éviter maïs sur maïs)',
            'Enfouir les résidus de récolte',
            'Choisir des hybrides résistants ou tolérants',
            'Semis dans de bonnes conditions de drainage',
        ],
        'urgence': 'moyenne',
    },

    'Corn_(maize)___Common_rust_': {
        'description': 'Rouille commune du maïs causée par Puccinia sorghi. Pustules brun-rougeâtre sur les deux faces des feuilles.',
        'traitement': [
            'Fongicide triazole si infection sévère avant la floraison',
            'Traiter tôt pour meilleur résultat économique',
            'Une seule application suffit généralement',
        ],
        'prevention': [
            'Utiliser des hybrides résistants à la rouille',
            'Semis précoce pour éviter les périodes à risque',
            'Surveiller régulièrement les champs dès mi-saison',
        ],
        'urgence': 'faible',
    },

    'Corn_(maize)___Northern_Leaf_Blight': {
        'description': 'Helminthosporiose du maïs causée par Exserohilum turcicum. Grandes taches elliptiques gris-verdâtre sur les feuilles.',
        'traitement': [
            'Appliquer un fongicide strobilurine ou triazole',
            'Traiter avant la floraison pour protéger la canopée supérieure',
            'Répéter si les conditions favorables persistent (humidité, fraîcheur)',
        ],
        'prevention': [
            'Rotation des cultures sur 2-3 ans',
            'Labourer pour enfouir les résidus contaminés',
            'Choisir des hybrides avec résistance partielle',
            'Éviter les densités de semis trop élevées',
        ],
        'urgence': 'moyenne',
    },

    'Corn_(maize)___healthy': {
        'description': '✅ Votre maïs est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Rotation des cultures recommandée',
            'Surveillance hebdomadaire des parcelles',
            'Fertilisation adaptée aux besoins du sol',
            'Gestion des résidus de récolte',
        ],
        'urgence': 'aucune',
    },

    # ─── GRAPE ───────────────────────────────────────────────────────────────
    'Grape___Black_rot': {
        'description': 'Pourriture noire de la vigne causée par Guignardia bidwellii. Taches brunes sur feuilles, fruits momifiés noirs.',
        'traitement': [
            'Traitement fongicide urgent (myclobutanil, mancozèbe, captan)',
            'Retirer et détruire tous les raisins momifiés restant sur la vigne',
            'Traiter toutes les 7-10 jours en période de croissance active',
            'Associer un fongicide de contact et un systémique',
        ],
        'prevention': [
            'Tailler sévèrement et éliminer les sarments infectés en hiver',
            'Ramasser et brûler les grappes momifiées',
            'Commencer les traitements préventifs dès le débourrement',
            'Assurer une bonne aération de la vigne par relevage et effeuillage',
        ],
        'urgence': 'haute',
    },

    'Grape___Esca_(Black_Measles)': {
        'description': 'Esca (rougeot parasitaire) causé par un complexe de champignons (Phaeomoniella, Phaeoacremonium). Maladie du bois très grave.',
        'traitement': [
            'Aucun traitement curatif chimique homologué disponible',
            'Tailler et éliminer les parties atteintes bien en dessous des symptômes',
            'Protéger les plaies de taille avec un mastic fongicide',
            'Dans les cas graves, arracher et replanter avec du matériel sain',
        ],
        'prevention': [
            'Désinfecter systématiquement les outils de taille',
            'Éviter les tailles par temps humide ou pluvieux',
            'Protéger toutes les plaies de taille immédiatement',
            'Utiliser du matériel végétal certifié sain',
        ],
        'urgence': 'haute',
    },

    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'description': 'Brûlure des feuilles de vigne causée par Isariopsis clavispora. Taches angulaires brunes sur le feuillage.',
        'traitement': [
            'Appliquer un fongicide à base de cuivre ou mancozèbe',
            'Traiter en fin de saison pour réduire l\'inoculum',
            'Supprimer les feuilles très atteintes',
        ],
        'prevention': [
            'Bonne aération de la vigne par taille et palissage',
            'Éviter l\'excès d\'humidité au niveau du feuillage',
            'Traitement préventif en fin de saison',
        ],
        'urgence': 'faible',
    },

    'Grape___healthy': {
        'description': '✅ Votre vigne est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Programme de traitements préventifs anti-mildiou et oïdium',
            'Taille et palissage réguliers',
            'Surveillance des populations d\'insectes',
            'Gestion raisonnée de l\'irrigation',
        ],
        'urgence': 'aucune',
    },

    # ─── ORANGE ──────────────────────────────────────────────────────────────
    'Orange___Haunglongbing_(Citrus_greening)': {
        'description': 'Huanglongbing (HLB) ou verdissement des agrumes, causé par la bactérie Candidatus Liberibacter. Maladie incurable et mortelle pour l\'arbre.',
        'traitement': [
            'Aucun traitement curatif existant — la maladie est incurable',
            'Arracher et détruire immédiatement les arbres infectés',
            'Désinfecter tout le matériel ayant touché les arbres malades',
            'Signaler la maladie aux autorités phytosanitaires locales',
        ],
        'prevention': [
            'Contrôler et éliminer le psylle asiatique (vecteur de la maladie)',
            'Utiliser uniquement du matériel végétal certifié et sain',
            'Inspecter régulièrement les vergers pour détecter les premiers symptômes',
            'Mettre en place des filets anti-insectes sur les jeunes plants',
        ],
        'urgence': 'critique',
    },

    # ─── PEACH ───────────────────────────────────────────────────────────────
    'Peach___Bacterial_spot': {
        'description': 'Tache bactérienne du pêcher causée par Xanthomonas arboricola pv. pruni. Taches angulaires sur feuilles, fruits et rameaux.',
        'traitement': [
            'Appliquer un bactéricide à base de cuivre (bouillie bordelaise) dès les premiers symptômes',
            'Traiter toutes les 7-14 jours en période humide et chaude',
            'Éliminer et brûler les branches et feuilles fortement infectées',
            'Éviter de travailler dans le verger par temps humide pour limiter la propagation',
        ],
        'prevention': [
            'Choisir des variétés résistantes ou tolérantes à la bactériose',
            'Désinfecter les outils de taille à l\'alcool ou à l\'eau de javel diluée',
            'Améliorer la circulation d\'air par une taille régulière et adaptée',
            'Arroser à la base, éviter absolument de mouiller le feuillage',
            'Traitement préventif au cuivre en automne après la chute des feuilles',
        ],
        'urgence': 'haute',
    },

    'Peach___healthy': {
        'description': '✅ Votre pêcher est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Traitement préventif au cuivre en hiver (bouillie bordelaise)',
            'Taille annuelle pour bonne aération de l\'arbre',
            'Surveiller l\'apparition de cloque du pêcher au printemps',
            'Fertilisation équilibrée, éviter les excès d\'azote',
        ],
        'urgence': 'aucune',
    },

    # ─── PEPPER ──────────────────────────────────────────────────────────────
    'Pepper,_bell___Bacterial_spot': {
        'description': 'Tache bactérienne du poivron causée par Xanthomonas campestris pv. vesicatoria. Taches aqueuses sur feuilles et fruits.',
        'traitement': [
            'Appliquer un bactéricide cuivrique dès l\'apparition des symptômes',
            'Retirer et détruire les plants très infectés',
            'Traiter toutes les 5-7 jours en conditions chaudes et humides',
            'Éviter de travailler dans la parcelle après la pluie ou la rosée',
        ],
        'prevention': [
            'Utiliser des semences certifiées et des plants sains',
            'Rotation des cultures sur 3-4 ans (éviter solanacées)',
            'Arrosage goutte-à-goutte pour éviter de mouiller le feuillage',
            'Désinfecter les outils et les serres entre chaque cycle de culture',
        ],
        'urgence': 'haute',
    },

    'Pepper,_bell___healthy': {
        'description': '✅ Votre poivron est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Rotation des cultures recommandée',
            'Arrosage régulier sans excès',
            'Surveiller les pucerons et aleurodes',
            'Tuteurage pour éviter que les fruits touchent le sol',
        ],
        'urgence': 'aucune',
    },

    # ─── POTATO ──────────────────────────────────────────────────────────────
    'Potato___Early_blight': {
        'description': 'Alternariose de la pomme de terre causée par Alternaria solani. Taches concentriques brunes sur les feuilles basses.',
        'traitement': [
            'Appliquer un fongicide à base de mancozèbe, chlorothalonil ou azoxystrobine',
            'Commencer les traitements dès l\'apparition des premières taches',
            'Répéter toutes les 7-14 jours selon la pression de la maladie',
            'Supprimer les feuilles atteintes les plus basses',
        ],
        'prevention': [
            'Rotation des cultures sur 3-4 ans',
            'Utiliser des semences certifiées saines et résistantes',
            'Éviter les excès d\'azote qui favorisent la sensibilité',
            'Arrosage en matinée pour que les feuilles sèchent rapidement',
        ],
        'urgence': 'moyenne',
    },

    'Potato___Late_blight': {
        'description': 'Mildiou de la pomme de terre causé par Phytophthora infestans. Maladie très destructrice responsable de la grande famine irlandaise.',
        'traitement': [
            'Traitement fongicide URGENT à base de cuivre ou de métalaxyl',
            'Détruire immédiatement les plants très infectés (ne pas composter)',
            'Traiter les plants voisins en traitement préventif d\'urgence',
            'Répéter tous les 5-7 jours en conditions favorables à la maladie',
        ],
        'prevention': [
            'Utiliser des variétés résistantes au mildiou',
            'Surveiller les bulletins d\'alerte mildiou de votre région',
            'Traitement préventif cuivrique en période à risque (temps frais et humide)',
            'Éliminer les repousses de pommes de terre spontanées',
            'Ne jamais arroser le soir — les feuilles doivent sécher avant la nuit',
        ],
        'urgence': 'critique',
    },

    'Potato___healthy': {
        'description': '✅ Votre culture de pommes de terre est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Surveiller régulièrement l\'apparition de symptômes de mildiou',
            'Rotation des cultures sur 3-4 ans minimum',
            'Utiliser des semences certifiées',
            'Buttage régulier pour protéger les tubercules',
        ],
        'urgence': 'aucune',
    },

    # ─── RASPBERRY ───────────────────────────────────────────────────────────
    'Raspberry___healthy': {
        'description': '✅ Votre framboisier est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Tailler les cannes après la récolte',
            'Surveiller les pucerons et acariens',
            'Maintenir un sol bien drainé',
            'Traitement préventif anti-botrytis en floraison',
        ],
        'urgence': 'aucune',
    },

    # ─── SOYBEAN ─────────────────────────────────────────────────────────────
    'Soybean___healthy': {
        'description': '✅ Votre culture de soja est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Rotation des cultures avec des céréales',
            'Surveillance des maladies fongiques en période humide',
            'Gestion des adventices pour limiter la concurrence',
            'Inoculation rhizobium pour optimiser la fixation d\'azote',
        ],
        'urgence': 'aucune',
    },

    # ─── SQUASH ──────────────────────────────────────────────────────────────
    'Squash___Powdery_mildew': {
        'description': 'Oïdium de la courge causé par Podosphaera xanthii. Feutrage blanc poudreux sur les feuilles réduisant la photosynthèse.',
        'traitement': [
            'Appliquer du soufre mouillable dès les premiers symptômes',
            'Utiliser du bicarbonate de potassium dilué (alternative bio)',
            'Fongicide systémique (myclobutanil, tétraconazole) si infection sévère',
            'Retirer les feuilles très atteintes pour limiter la propagation',
        ],
        'prevention': [
            'Bonne aération entre les plants (espacement suffisant)',
            'Éviter les excès d\'engrais azotés',
            'Choisir des variétés résistantes à l\'oïdium',
            'Arrosage à la base, ne jamais mouiller le feuillage',
        ],
        'urgence': 'moyenne',
    },

    # ─── STRAWBERRY ──────────────────────────────────────────────────────────
    'Strawberry___Leaf_scorch': {
        'description': 'Brûlure des feuilles du fraisier causée par Diplocarpon earlianum. Taches pourpres sur feuilles pouvant causer leur dessèchement.',
        'traitement': [
            'Appliquer un fongicide à base de captane ou myclobutanil',
            'Retirer et détruire toutes les feuilles atteintes',
            'Traiter toutes les 10-14 jours en période humide',
        ],
        'prevention': [
            'Renouveler les plantations tous les 3-4 ans',
            'Éviter l\'arrosage par aspersion sur le feuillage',
            'Pailler pour éviter les éclaboussures de sol',
            'Bonne aération entre les rangs',
        ],
        'urgence': 'moyenne',
    },

    'Strawberry___healthy': {
        'description': '✅ Votre fraisier est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Renouveler les plantations régulièrement',
            'Surveiller l\'oïdium et la botrytis en floraison',
            'Pailler pour éviter le contact fruits-sol',
            'Irrigation goutte-à-goutte recommandée',
        ],
        'urgence': 'aucune',
    },

    # ─── TOMATO ──────────────────────────────────────────────────────────────
    'Tomato___Bacterial_spot': {
        'description': 'Tache bactérienne de la tomate causée par Xanthomonas vesicatoria. Taches aqueuses sombres sur feuilles et fruits.',
        'traitement': [
            'Bactéricide cuivrique appliqué dès les premiers symptômes',
            'Traiter toutes les 5-7 jours en temps chaud et humide',
            'Éliminer les plants fortement infectés',
            'Ne pas travailler dans la parcelle par temps humide',
        ],
        'prevention': [
            'Semences certifiées et plants sains',
            'Rotation des cultures (3-4 ans sans solanacées)',
            'Arrosage goutte-à-goutte uniquement',
            'Désinfection des outils et tuteurs entre chaque saison',
        ],
        'urgence': 'haute',
    },

    'Tomato___Early_blight': {
        'description': 'Alternariose de la tomate causée par Alternaria solani. Taches brunes concentriques sur feuilles basses évoluant vers le haut.',
        'traitement': [
            'Fongicide à base de chlorothalonil, mancozèbe ou azoxystrobine',
            'Retirer les feuilles infectées immédiatement',
            'Traiter toutes les 7-10 jours en période humide',
            'Arroser le matin pour que les feuilles sèchent dans la journée',
        ],
        'prevention': [
            'Rotation des cultures sur 3-4 ans',
            'Paillage du sol pour éviter les éclaboussures',
            'Espacement suffisant entre les plants',
            'Fertilisation équilibrée (éviter excès d\'azote)',
        ],
        'urgence': 'moyenne',
    },

    'Tomato___Late_blight': {
        'description': 'Mildiou de la tomate causé par Phytophthora infestans. Maladie dévastatrice à propagation très rapide par temps frais et humide.',
        'traitement': [
            'Traitement fongicide URGENT (cuivre, métalaxyl, mandipropamide)',
            'Éliminer et détruire les plants très infectés immédiatement',
            'Traiter les plants voisins en préventif d\'urgence',
            'Répéter tous les 5-7 jours tant que les conditions sont favorables',
        ],
        'prevention': [
            'Surveiller les bulletins d\'alerte mildiou locaux',
            'Arrosage uniquement à la base — jamais le soir',
            'Bonne aération entre les plants (tuteurage, taille)',
            'Traitement préventif cuivrique par temps frais et humide',
            'Éliminer les repousses de tomates spontanées',
        ],
        'urgence': 'critique',
    },

    'Tomato___Leaf_Mold': {
        'description': 'Cladosporiose de la tomate causée par Passalora fulva. Feutrage olive sous les feuilles, jaunissement sur le dessus. Fréquent en serre.',
        'traitement': [
            'Fongicide à base de chlorothalonil ou mancozèbe',
            'Retirer les feuilles atteintes',
            'Améliorer immédiatement la ventilation de la serre',
            'Traiter toutes les 7-10 jours',
        ],
        'prevention': [
            'Maintenir l\'humidité relative en dessous de 85% en serre',
            'Ventilation et aération optimales',
            'Éviter les variations brusques de température',
            'Choisir des variétés résistantes pour la culture sous abri',
        ],
        'urgence': 'moyenne',
    },

    'Tomato___Septoria_leaf_spot': {
        'description': 'Septoriose de la tomate causée par Septoria lycopersici. Petites taches rondes avec centre clair et bordure sombre sur feuilles basses.',
        'traitement': [
            'Fongicide à base de chlorothalonil, mancozèbe ou cuivre',
            'Supprimer les feuilles infectées à la base',
            'Traiter toutes les 7-10 jours',
            'Alterner les familles de fongicides pour éviter les résistances',
        ],
        'prevention': [
            'Rotation des cultures sur 3 ans',
            'Paillage du sol pour limiter les éclaboussures',
            'Éviter de travailler dans les plants mouillés',
            'Bonne aération par tuteurage et taille des gourmands',
        ],
        'urgence': 'moyenne',
    },

    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'description': 'Acarien tétranyque (Tetranychus urticae) provoquant un jaunissement et dessèchement des feuilles. Prolifère par temps chaud et sec.',
        'traitement': [
            'Appliquer un acaricide homologué (abamectine, bifénazate)',
            'Pulvériser de l\'eau froide sous les feuilles (gêne les acariens)',
            'Huile horticole ou savon insecticide en début d\'infestation',
            'Répéter le traitement après 5-7 jours pour éliminer les œufs',
        ],
        'prevention': [
            'Maintenir une humidité suffisante autour des plants',
            'Favoriser les auxiliaires naturels (acariens prédateurs)',
            'Éviter les excès d\'engrais azotés qui favorisent les acariens',
            'Inspecter régulièrement la face inférieure des feuilles',
        ],
        'urgence': 'haute',
    },

    'Tomato___Target_Spot': {
        'description': 'Tache cible de la tomate causée par Corynespora cassiicola. Taches brunes avec anneaux concentriques sur feuilles, tiges et fruits.',
        'traitement': [
            'Fongicide à base d\'azoxystrobine, chlorothalonil ou mancozèbe',
            'Retirer les feuilles et fruits atteints',
            'Traiter toutes les 7-14 jours',
        ],
        'prevention': [
            'Bonne aération entre les plants',
            'Éviter les excès d\'humidité',
            'Rotation des cultures',
            'Paillage du sol',
        ],
        'urgence': 'moyenne',
    },

    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'description': 'Virus de l\'enroulement jaune de la tomate (TYLCV) transmis par l\'aleurode Bemisia tabaci. Feuilles enroulées et jaunissantes, plant rabougri.',
        'traitement': [
            'Aucun traitement curatif contre le virus lui-même',
            'Éliminer et détruire les plants infectés pour limiter la propagation',
            'Traiter les aleurodes (vecteurs) avec un insecticide systémique',
            'Utiliser des pièges jaunes englués pour surveiller les aleurodes',
        ],
        'prevention': [
            'Utiliser des variétés résistantes au TYLCV (indispensable en zone à risque)',
            'Mettre en place des filets anti-insectes (50 mailles) sur les serres',
            'Lutte biologique contre les aleurodes (Encarsia formosa)',
            'Éliminer les mauvaises herbes hôtes autour des parcelles',
            'Ne pas replanter des tomates sur une parcelle infectée la même saison',
        ],
        'urgence': 'critique',
    },

    'Tomato___Tomato_mosaic_virus': {
        'description': 'Virus de la mosaïque de la tomate (ToMV). Mosaïque vert clair/foncé sur les feuilles, déformation et réduction des rendements.',
        'traitement': [
            'Aucun traitement curatif disponible contre le virus',
            'Arracher et détruire les plants très symptomatiques',
            'Désinfecter les outils avec de l\'alcool ou du lait écrémé dilué',
            'Se laver les mains après manipulation des plants infectés',
        ],
        'prevention': [
            'Utiliser des semences certifiées et des variétés résistantes (gène Tm-2)',
            'Désinfecter tous les outils, tuteurs et équipements régulièrement',
            'Lutter contre les pucerons (vecteurs secondaires)',
            'Éviter de fumer près des plants (le tabac est réservoir du virus)',
            'Ne pas introduire de plants du dehors sans quarantaine',
        ],
        'urgence': 'haute',
    },

    'Tomato___healthy': {
        'description': '✅ Votre tomate est en parfaite santé !',
        'traitement': [],
        'prevention': [
            'Arrosage régulier à la base pour éviter les maladies foliaires',
            'Tuteurage et taille des gourmands pour bonne aération',
            'Surveiller régulièrement sous les feuilles (acariens, aleurodes)',
            'Rotation des cultures recommandée chaque saison',
        ],
        'urgence': 'aucune',
    },
}


def get_recommendations(class_name: str) -> dict:
    """Retourne les recommandations pour une classe de maladie donnée."""
    default = {
        'description': 'Maladie identifiée — consultez un agronome local pour des conseils adaptés à votre région.',
        'traitement': [
            'Consulter immédiatement un expert agricole ou agronome local',
            'Prendre des photos et noter l\'évolution des symptômes',
            'Isoler les plants atteints pour limiter la propagation',
        ],
        'prevention': [
            'Surveiller régulièrement l\'ensemble de vos cultures',
            'Mettre en place une rotation des cultures',
            'Maintenir de bonnes conditions d\'hygiène dans la parcelle',
        ],
        'urgence': 'moyenne',
    }
    return RECOMMENDATIONS.get(class_name, default)