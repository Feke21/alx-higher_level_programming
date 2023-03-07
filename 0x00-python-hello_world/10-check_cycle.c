#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: singly linked list to check
 *
 * Return: 0 if no cycle. 1 if cycle is present
 */
int check_cycle(listint_t *list)
{
	listint_t *new = list;
	listint_t *main = list;

	if (list == NULL)
		return (0);

	while (new && main && main ->next)
	{
		new = new->next;
		main = main->next->next;
		if (new == main)
			return (1);
	}
	return (0);
}
