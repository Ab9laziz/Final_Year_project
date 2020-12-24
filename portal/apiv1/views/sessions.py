from django.shortcuts import get_object_or_404
from ...models import TrainingSession
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class TrainingAddPlayersAPIView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    def post(self, *args, **kwargs):
        data = self.request.data
        session_to_be_added = get_object_or_404(TrainingSession, id=data['session'])
        print(session_to_be_added)
        print(data)

        players = data['players']
        total_players = len(players)
        print(f"player count is {total_players}")
        added_players_count = int()

        for player in players:
            player_to_add = get_object_or_404(User, id=player)
            print(f"I am a player {player_to_add}")
            session_to_be_added.players.add(player_to_add)
            session_to_be_added.save()
            added_players_count +=1

        if total_players < added_players_count:
            return Response({"detail": "Some players were not added to group"}, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response({"detail": "players added to group"}, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        session_to_be_removed = get_object_or_404(TrainingSession, id=data['session'])

        players = data['players']
        total_players = len(players)
        print(f"player count is {total_players}")
        removed_players_count = int()

        for player in players:
            player_to_remove = get_object_or_404(User, id=player)
            print(f"I am a player {player_to_remove}")
            session_to_be_removed.players.remove(player_to_remove)
            session_to_be_removed.save()
            removed_players_count +=1

        if total_players < removed_players_count:
            return Response({"detail": "Some players were not removed from group"}, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response({"detail": "players removed from group"}, status=status.HTTP_200_OK)


class TrainingAddTrainersAPIView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    def post(self, *args, **kwargs):
        data = self.request.data
        session_to_be_added = get_object_or_404(TrainingSession, id=data['session'])

        trainers = data['trainers']
        total_trainers = len(trainers)
        added_trainers_count = int()

        for trainer in trainers:
            trainer_to_add = get_object_or_404(User, id=trainer)
            session_to_be_added.trainers.add(trainer_to_add)
            session_to_be_added.save()
            added_trainers_count +=1

        if total_trainers < added_trainers_count:
            return Response({"detail": "Some Trainers were not added to group"}, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response({"detail": "Trainers added to group"}, status=status.HTTP_200_OK)


