#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * lol
 */

int is_palindrome(listint_t **head)
{
	listint_t *end = *head;
	listint_t *front = *head;
	int count = 0, index = 0, sub = 0;

	if (*head == NULL)
		return (1);
	while (end->next != NULL)
	{
		end = end->next;
		count++;
	}
	if (front->n == end->n)
	{	
		while (sub <= (count / 2))
		{
			end = *head;
			for (index = 0; index < (count - sub); index++)
				end = end->next;
			if (front->n != end->n)
				return (0);
			else
			{
				sub++;
				front = front->next;
			}
		}
	}
	return (1);
}
