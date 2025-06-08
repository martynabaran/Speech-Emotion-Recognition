##################################################
#                                                #
#             MSP-PODCAST Database               #
#                                                #
#          The University of Texas at Dallas     #
#  Multimodal Signal Processing (MSP) Laboratory # 
#             Contact: Prof. Carlos Busso        # 
#              Release Emo-challenge-odyssey     #   
#                                                #
##################################################



The corpus includes:

	- readme.txt (this file)

	- Speaker_ids.txt (speaker information)

	- Partition.txt (suggested partition for Train, Development, Test3 sets)

	- Folder Audios (it contains the audio files of the corpus - 119,421 speaking turns)

	- Folder "Labels/" (emotional labels for the corpus)

		- labels.txt (raw file with emotional annotation information) 

		- labels_consensus.csv (aggregated annotations in CSV format)

		- labels_detailed.csv (detailed individual annotations in CSV format)

		- labels_consensus.json (aggregated annotations in JSON format)

		- labels_detailed.json (detailed individual annotations in JSON format)

	- Folder Transcripts (it contains human-labeled audio transcripts of the corpus - 116,221 speaking turns have been transcribed)

        - Folder ForceAligned (it contains force alignment results based on the manual transcripts of the corpus - 116,221 speaking turns have been aligned)
	
	
 

************************************

    Partition 

************************************



The proposed partition attempts to create speaker-independent datasets for Train, Development.


- Development set: We use segments from 714 speakers - 31,961 segments

- Train set: We use the remaining speech samples from 2,114 speakers - 84,260 segments.

- Test3 Set: This partition comprises 3,200 unique segments from 256 speakers, for which the labels are not publicly available. The segments have been curated to maintain a balanced representation based on primary categorical emotions (Anger, Sadness, Happiness, Surprise, Fear, Disgust, Contempt, Neutral). The release only includes the audio information. The labels, speaker information, transcription, and forced alignment information have been hidden. The researchers will be able to evaluate the results of primary emotions and emotional attributes on this partition using a web-based interface.

************************************

    Emotional Labels 

************************************



The emotional labels are in the folder "Labels". The main file is labels.txt, which contains all the emotional evaluations collected for this set. The format of this file is explained below. In addition, we include the emotional labels and meta-information in CSV and JSON format:



CSV format: 	[labels_consensus.csv, 	labels_detailed.csv]

JSON format: 	[labels_consensus.json, labels_detailed.json]



labels_consensus => include emotion labels after aggregating the annotations (primary emotion, secondary emotions, emotional attributes), gender, speaker and split set information.

labels_detailed => individual annotation provided by each worker to each sentence 





The database label file (labels.txt) is organized as follows:



The annotations of each audio file are shown together with an empty line separating the annotations of different files. This is an example of one file:



MSP-PODCAST_0001_0139.wav; N; A:2.400000; V:4.000000; D:2.800000;

WORKER00000001; Other-confused; Concerned,Confused; A:3.000000; V:3.000000; D:4.000000;

WORKER00000018; Neutral; Neutral; A:1.000000; V:4.000000; D:2.000000;

WORKER00000021; Neutral; Neutral; A:3.000000; V:4.000000; D:2.000000;

WORKER00000028; Neutral; Neutral; A:2.000000; V:4.000000; D:3.000000;

WORKER00000044; Surprise; Neutral,Surprise; A:3.000000; V:5.000000; D:3.000000;



[next file] ...



Explanation about the annotation:

We are collecting three set of information:



1-) Arousal, valence and dominance

	- we use Self-Assessment Manikin (SAM) where rankings go from 1 to 7

	- valence (1-very negative; 7-very positive)

	- arousal (1-very calm; 7-very active)

	- dominance (1-very weak; 7-very strong)



2-) Primary emotions (categorical)

	- only one option is allowed

	- you can say "other" and define your own emotional class



Primary emotions and the consensus emotion code:

Angry		(A)

Sad		(S)

Happy		(H)

Surprise	(U)

Fear		(F)

Disgust		(D)

Contempt	(C)

Neutral		(N)

Other		(O)

No agreement    (X)	//when there is no plurality voting winner between the above emotions





3-) Secondary emotions

	- you can select as many emotional classes as you want

	- you can also select "other" and specify the emotional class



Secondary emotions:



Angry

Sad

Happy

Amused

Neutral

Frustrated

Depressed

Surprise

Concerned

Disgust

Disappointed

Excited

Confused

Annoyed

Fear

Contempt

Other



Few explanations about this format:

1)- the first line brings a summary of the sentence. First, it provides the name of the segment (in this case MSP-PODCAST_0001_0139.wav). Then it provides the consensus (plurality vote) of primary emotion (in this case "N" for Neutral since 3 out of 5 people selected this option). Then, it provides the average values for A: activation (2.4), V:valence (4.0) and D:dominance (2.8)



2)- The next lines provide individual evaluations from evaluators

	a) first, it is the ID that we assigned to workers (e.g., WORKER00000001 for the first evaluator).

	b) Then, it lists the primary emotion ('Other-confused'). They can choose from Angry, Sad, Happy, Surprise, Fear, Disgust, Contempt, Neutral and Other. In the first case they chose Other, and then they suggested the label "confused"

	c) Then, it lists the secondary emotion ('Concerned,Confused'). They can choose from the following list: Angry, Sad, Happy, Amused, Neutral, Frustrated, Depressed, Surprise, Concerned, Disgust, Disappointed, Excited, Confused, Annoyed, Fear, Contempt, Other. A key difference here is that they can choose multiple options as opposed to primary emotions where they can only select one. 

	d) The values for arousal, valence and dominance (A:3.000000; V:3.000000; D:4.000000;)



************************************

    Speaker Information

************************************



We have manually annotated the speaker identity of all sentences corresponding. The file Speaker_ids.txt provides the details. It also provides the gender of the speakers. 



************************************

  Transcripts and ForceAligned

************************************



We have transcribed the entire corpus. We provide human transcriptions in the zip file 'Transcripts.zip' and the corresponding forced alignment results in 'ForceAligned.zip'. The transcriptions are labeled by REV.com (https://www.rev.com), we use Montreal-Forced-Aligner (MFA, https://montreal-forced-aligner.readthedocs.io/en/latest/) to obtain the force alignment results. The pretrained acoustic model for forced alignment was based on the LibriSpeech dataset. The transcriptions for the Test3 set have not been included in the release.


- The provided file format in the 'Transcripts.zip' is plain text (e.g., MSP-PODCAST_0001_0143.txt)

- The provided file format in the 'ForceAligned.zip' is TextGrid format (e.g., MSP-PODCAST_0001_0143.TextGrid), users can directly load the file via Praat (https://www.fon.hum.uva.nl/praat/)



************************************

    Description of the database

************************************



For further information on the corpus, please read:



Reza Lotfian and Carlos Busso, "Building naturalistic emotionally balanced speech corpus by retrieving emotional speech from existing podcast recordings," IEEE Transactions on Affective Computing, vol. 10, no. 4, pp. 471-483, October-December 2019.



************************************

    Contact Information

************************************



If you have any feedback or question, please contact Prof. Carlos Busso (busso@utdallas.edu)



Prof. Carlos Busso

Professor 

The University of Texas at Dallas 

Erik Jonsson School of Engineering and Computer Science

Department of Electrical and Computer Engineering, 

800 West Campbell Road, ECSN 

Richardson, TX  75080-3021 

busso@utdallas.edu



